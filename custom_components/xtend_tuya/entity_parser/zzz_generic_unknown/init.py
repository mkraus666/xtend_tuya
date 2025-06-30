
"""Generic fallback entity parser that exposes all un‑described DP codes as diagnostic sensors (disabled by default)."""

from __future__ import annotations

from typing import Any, Dict, Tuple
from homeassistant.const import Platform
from homeassistant.components.sensor import (
    SensorStateClass,
)
from homeassistant.const import (
    EntityCategory,
)

from ..entity_parser import XTCustomEntityParser
from ...const import XTDPCode, CROSS_CATEGORY_DEVICE_DESCRIPTOR
from ...sensor import XTSensorEntityDescription, SensorDeviceClass

# Build once at import time: create a generic descriptor for every DP code
# that doesn't already have a dedicated description in the core SENSORS mapping.
try:
    from ...sensor import SENSORS as _CORE_SENSORS
    _already_described = {
        desc.key for tuples in _CORE_SENSORS.values() for desc in tuples
    }
except Exception:
    _already_described = set()

_GENERIC_DESCRIPTORS: Tuple[XTSensorEntityDescription, ...] = tuple(
    XTSensorEntityDescription(
        key=code,
        name=str(code).replace("_", " ").title(),
        translation_key=None,
        state_class=SensorStateClass.MEASUREMENT,
        device_class=None,
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_registry_enabled_default=False,
    )
    for code in XTDPCode
    if code not in _already_described
)

_GENERIC_SENSOR_MAP: Dict[str, Tuple[XTSensorEntityDescription, ...]] = {
    CROSS_CATEGORY_DEVICE_DESCRIPTOR: _GENERIC_DESCRIPTORS
}


def get_plugin_instance():
    return GenericUnknownEntityParser()


class GenericUnknownEntityParser(XTCustomEntityParser):

    def get_descriptors_to_merge(self, platform: Platform) -> Any:
        if platform == Platform.SENSOR:
            return _GENERIC_SENSOR_MAP
        return None