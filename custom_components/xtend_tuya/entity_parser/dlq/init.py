
"""Entity parser plug‑in for Tuya 'dlq' 3‑phase power switch."""

from __future__ import annotations

from typing import Any
from homeassistant.const import Platform

from ..entity_parser import XTCustomEntityParser

from .sensor import get_dlq_sensor_descriptors

def get_plugin_instance():
    return DLQEntityParser()

class DLQEntityParser(XTCustomEntityParser):

    def get_descriptors_to_merge(self, platform: Platform) -> Any:
        if platform == Platform.SENSOR:
            return get_dlq_sensor_descriptors()
        return None
