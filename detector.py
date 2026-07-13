"""
Isolation Forest inference pipeline.

Responsibilities
----------------
1. Load the trained model.
2. Convert a device dictionary into a numerical feature vector.
3. Perform anomaly detection.
4. Return a simple result dictionary.
"""

from pathlib import Path

import joblib
import numpy as np


MODEL_PATH = Path("model.pkl")


class DeviceDetector:
    """Runs anomaly detection on mocked mobile device information."""

    def __init__(self):
        if not MODEL_PATH.exists():
            raise FileNotFoundError(
                "Model not found. Run 'python train.py' first."
            )

        self.model = joblib.load(MODEL_PATH)

    def _encode_network(self, network: str) -> int:
        """
        Encode network type.

        private_wifi -> 0
        public_wifi  -> 1
        """

        mapping = {
            "private_wifi": 0,
            "public_wifi": 1,
        }

        return mapping.get(network, 1)

    def _build_feature_vector(self, device: dict) -> np.ndarray:
        """
        Convert a device dictionary into the feature order expected
        by the Isolation Forest.
        """

        features = [
            device["os_version"],
            self._encode_network(device["network"]),
            int(device["vpn_enabled"]),
            int(device["developer_mode"]),
            int(device["rooted"]),
            int(device["bootloader_unlocked"]),
            int(device["screen_lock"]),
            int(device["play_protect"]),
            int(device["usb_debugging"]),
            int(device["unknown_sources"]),
        ]

        return np.array(features).reshape(1, -1)

    def _map_risk(self, score: float) -> str:
        """
        Convert anomaly score into a human-readable risk level.

        Isolation Forest scores are negative.
        More negative means more anomalous.
        """

        if score > -0.62:
            return "Low"

        if score > -0.70:
            return "Medium"

        return "Critical"

    def analyze(self, device: dict) -> dict:
        """
        Analyze a device.

        Returns a dictionary suitable for printing
        or passing to the LLM.
        """

        features = self._build_feature_vector(device)

        prediction = int(self.model.predict(features)[0])

        score = float(self.model.score_samples(features)[0])

        risk = self._map_risk(score)

        return {
            "prediction": prediction,
            "score": round(score, 4),
            "risk": risk,
            "allow_llm": risk != "Critical",
        }