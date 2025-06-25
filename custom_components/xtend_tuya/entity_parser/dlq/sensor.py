
"""DLQ (3-phase Power Switch) specific sensor mapping for xtend_tuya."""

from __future__ import annotations

from typing import Tuple
from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorStateClass,
)

from ...sensor import XTSensorEntityDescription
from ...const import XTDPCode

# Sensors for each phase voltage, current, power, temperature, and cumulative energy.
_DLQ_SENSORS: tuple[XTSensorEntityDescription, ...] = (
    # Voltages (divide value by 10; handled by Tuya scale metadata)
    XTSensorEntityDescription(
        key=XTDPCode.VOL_A,
        translation_key="voltage_a",
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    XTSensorEntityDescription(
        key=XTDPCode.VOL_B,
        translation_key="voltage_b",
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    XTSensorEntityDescription(
        key=XTDPCode.VOL_C,
        translation_key="voltage_c",
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    # Currents (divide value by 1000; handled by Tuya scale metadata)
    XTSensorEntityDescription(
        key=XTDPCode.CUR_A,
        translation_key="current_a",
        device_class=SensorDeviceClass.CURRENT,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    XTSensorEntityDescription(
        key=XTDPCode.CUR_B,
        translation_key="current_b",
        device_class=SensorDeviceClass.CURRENT,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    XTSensorEntityDescription(
        key=XTDPCode.CUR_C,
        translation_key="current_c",
        device_class=SensorDeviceClass.CURRENT,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    # Instantaneous Power per phase
    XTSensorEntityDescription(
        key=XTDPCode.PW_A,
        translation_key="power_a",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    XTSensorEntityDescription(
        key=XTDPCode.PW_B,
        translation_key="power_b",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    XTSensorEntityDescription(
        key=XTDPCode.PW_C,
        translation_key="power_c",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    # Total Power
    XTSensorEntityDescription(
        key=XTDPCode.PW_T,
        translation_key="power_total",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    # Temperatures
    XTSensorEntityDescription(
        key=XTDPCode.TEMP_A,
        translation_key="temperature_a",
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    XTSensorEntityDescription(
        key=XTDPCode.TEMP_B,
        translation_key="temperature_b",
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    XTSensorEntityDescription(
        key=XTDPCode.TEMP_C,
        translation_key="temperature_c",
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    XTSensorEntityDescription(
        key=XTDPCode.TEMP_N,
        translation_key="temperature_neutral",
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    # Leakage current
    XTSensorEntityDescription(
        key=XTDPCode.LEAKAGE_CURRENT,
        translation_key="leakage_current",
        device_class=SensorDeviceClass.CURRENT,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,  # disable by default
    ),
    # Energy counters (kWh) per phase + total
    XTSensorEntityDescription(
        key=XTDPCode.EP_A,
        translation_key="energy_total_a",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    XTSensorEntityDescription(
        key=XTDPCode.EP_B,
        translation_key="energy_total_b",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    XTSensorEntityDescription(
        key=XTDPCode.EP_C,
        translation_key="energy_total_c",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    XTSensorEntityDescription(
        key=XTDPCode.EP_T,
        translation_key="energy_total_all",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
)

# Map under the Tuya device category "dlq"
DLQ_SENSOR_DESCRIPTORS: dict[str, tuple[XTSensorEntityDescription, ...]] = {
    "dlq": _DLQ_SENSORS,
}

def get_dlq_sensor_descriptors() -> dict[str, tuple[XTSensorEntityDescription, ...]]:
    """Return the descriptors so the parser can merge them."""
    return DLQ_SENSOR_DESCRIPTORS
