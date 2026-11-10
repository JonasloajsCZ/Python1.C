#!/usr/bin/env python3
"""
IoT Sensor Network Simulator & Analytics Engine
----------------------------------------------
Tento skript simuluje asynchronní sběr dat z několika průmyslových senzoru,
provádí real-time analýzu anomálií a generuje závěrečný report.

Ukazuje pokročilé koncepty: Asyncio, OOP, Dataclasses, Typování a Logging.
"""

import asyncio
import datetime
import logging
import random
import sys
from dataclasses import dataclass, field
from typing import Dict, List, Optional

# Nastavení profesionálního logování do konzole
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger("IoT_Engine")


@dataclass(frozen=True)
class TelemetryData:
    """Imutabilní datová struktura pro telemetrická data."""
    sensor_id: str
    timestamp: datetime.datetime
    temperature: float
    humidity: float
    voltage: float


@dataclass
class SensorMetrics:
    """Třída pro udržování statistik jednotlivých senzorů."""
    sensor_id: str
    readings_count: int = 0
    temp_sum: float = 0.0
    anomalies_detected: int = 0
    history: List[float] = field(default_factory=list)

    @property
    def average_temperature(self) -> float:
        if self.readings_count == 0:
            return 0.0
        return self.temp_sum / self.readings_count


class AnalyticsEngine:
    """Hlavní analytický engine pro zpracování dat a detekci anomálií."""
    
    def __init__(self, temp_threshold: float = 85.0):
        self.temp_threshold = temp_threshold
        self.metrics_registry: Dict[str, SensorMetrics] = {}

    def process_reading(self, data: TelemetryData) -> bool:
        """
        Zpracuje nový odečet ze senzoru a zkontroluje anomálie.
        Vrací True, pokud byla detekována anomálie.
        """
        if data.sensor_id not in self.metrics_registry:
            self.metrics_registry[data.sensor_id] = SensorMetrics(sensor_id=data.sensor_id)
        
        metrics = self.metrics_registry[data.sensor_id]
        metrics.readings_count += 1
        metrics.temp_sum += data.temperature
        metrics.history.append(data.temperature)

        # Logika pro detekci anomálií (přehřátí)
        if data.temperature > self.temp_threshold:
            metrics.anomalies_detected += 1
            logger.warning(
                f"🚨 ANOMÁLIE DETEKOVÁNA! Senzor {data.sensor_id} hlásí "
                f"kritickou teplotu {data.temperature}°C (Limit: {self.temp_threshold}°C)"
            )
            return True
        return False

    def generate_ascii_report(self) -> None:
        """Vygeneruje vizuálně atraktivní report do konzole."""
        print("\n" + "="*60)
        print("📊 ZÁVĚREČNÝ ANALYTICKÝ REPORT SÍTĚ SENZORŮ")
        print("="*60)
        
        for sensor_id, metrics in self.metrics_registry.items():
            avg_t = metrics.average_temperature
            anom = metrics.anomalies_detected
            
            print(f"\nSenzor: [ {sensor_id} ]")
            print(f"  └─ Celkem odečtů:  {metrics.readings_count}")
            print(f"  └─ Průměrná tepl.: {avg_t:.2s}°C")
            print(f"  └─ Počet anomálií: {anom if anom == 0 else f'🔥 {anom}'}")
            
            # Mini textový graf historie teploty
            if metrics.history:
                sparkline = "".join(["_" if t < 40 else "▄" if t < 70 else "█" for t in metrics.history[-20:]])
                print(f"  └─ Vývoj teploty:  [{sparkline}] (posledních 20 měření)")
                
        print("\n" + "="*60)


class VirtualSensor:
    """Simulátor fyzického hardwarového senzoru běžící asynchronně."""
    
    def __init__(self, sensor_id: str, interval: float = 0.5):
        self.sensor_id = sensor_id
        self.interval = interval
        self._is_running = False

    async def start_streaming(self, queue: asyncio.Queue) -> None:
        """Spustí nekonečnou smyčku generování dat."""
        self._is_running = True
        logger.info(f"Senzor {self.sensor_id} byl úspěšně spuštěn.")
        
        try:
            while self._is_running:
                await asyncio.sleep(self.interval)
                
                # Simulace reálných dat s občasnou chybou/anomálií
                base_temp = 50.0 if "ZONE-A" in self.sensor_id else 65.0
                if random.random() > 0.95:  # 5% šance na anomálii
                    temperature = random.uniform(90.0, 110.0)
                else:
                    temperature = random.uniform(base_temp - 5, base_temp + 5)

                data = TelemetryData(
                    sensor_id=self.sensor_id,
                    timestamp=datetime.datetime.now(),
                    temperature=round(temperature, 2),
                    humidity=round(random.uniform(30.0, 60.0), 2),
                    voltage=round(random.uniform(3.2, 3.6), 2)
                )
                
                await queue.put(data)
                
        except asyncio.CancelledError:
            logger.info(f"Streamování senzoru {self.sensor_id} bylo zastaveno.")
        finally:
            self._is_running = False


async def main():
    """Hlavní asynchronní exekuční bod programu."""
    logger.info("Zahajuji inicializaci IoT monitorovacího systému...")
    
    # Inicializace fronty, analytického enginu a senzorů
    data_queue: asyncio.Queue[TelemetryData] = asyncio.Queue()
    engine = AnalyticsEngine(temp_threshold=80.0)
    
    sensors = [
        VirtualSensor(sensor_id="ZONE-A-TEMP-01", interval=0.2),
        VirtualSensor(sensor_id="ZONE-A-TEMP-02", interval=0.3),
        VirtualSensor(sensor_id="ZONE-B-CORE-01", interval=0.1),
    ]

    # Spuštění senzorů na pozadí jako asynchronní tasky
    sensor_tasks = [
        asyncio.create_task(sensor.start_streaming(data_queue)) 
        for sensor in sensors
    ]

    logger.info("Systém běží. Sbírám data po dobu 5 sekund...")
    
    # Asynchronní konzument dat, který běží paralelně se sběrem dat
    async def consumer():
        try:
            while True:
                data = await data_queue.get()
                engine.process_reading(data)
                data_queue.task_done()
        except asyncio.CancelledError:
            pass

    consumer_task = asyncio.create_task(consumer())

    # Necháme simulaci běžet 5 sekund
    await asyncio.sleep(5.0)

    # Čisté ukončení všech běžících tasků
    logger.info("Ukončuji sběr dat a vypínám senzory...")
    for task in sensor_tasks:
        task.cancel()
    
    await asyncio.gather(*sensor_tasks, return_exceptions=True)
    
    # Počkáme na zpracování zbylých dat ve frontě a ukončíme konzumenta
    await data_queue.join()
    consumer_task.cancel()
    await consumer_task

    # Vyobrazení výsledků
    engine.generate_ascii_report()
    logger.info("Systém byl bezpečně vypnut.")


if __name__ == "__main__":
    # Spuštění asynchronní hlavní funkce
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Program byl násilně ukončen uživatelem.")