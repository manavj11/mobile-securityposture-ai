"""
Train an Isolation Forest using synthetic mobile device data.

The model learns what "normal" devices look like.
Later we can score incoming devices for abnormal behaviour.
"""

import joblib
import numpy as np
from sklearn.ensemble import IsolationForest

MODEL_PATH = "model.pkl"

RANDOM_SEED = 42

np.random.seed(RANDOM_SEED)


def generate_normal_devices(samples: int = 500) -> np.ndarray:
    """
    Generate synthetic devices that represent typical users.

    Feature order:

    [
        os_version,
        network,
        vpn_enabled,
        developer_mode,
        rooted,
        bootloader_unlocked,
        screen_lock,
        play_protect,
        usb_debugging,
        unknown_sources
    ]
    """

    devices = []

    for _ in range(samples):

        os_version = np.random.randint(12, 15)

        network = np.random.choice(
            [0, 1],
            p=[0.8, 0.2],      # Mostly private WiFi
        )

        vpn = np.random.choice(
            [0, 1],
            p=[0.4, 0.6],
        )

        developer = np.random.choice(
            [0, 1],
            p=[0.9, 0.1],
        )

        rooted = 0
        bootloader = 0

        screen_lock = 1

        play_protect = 1

        usb_debugging = np.random.choice(
            [0, 1],
            p=[0.9, 0.1],
        )

        unknown_sources = np.random.choice(
            [0, 1],
            p=[0.9, 0.1],
        )

        devices.append([
            os_version,
            network,
            vpn,
            developer,
            rooted,
            bootloader,
            screen_lock,
            play_protect,
            usb_debugging,
            unknown_sources,
        ])

    return np.array(devices)


def train_model() -> None:
    """Train and persist the Isolation Forest."""

    training_data = generate_normal_devices()

    model = IsolationForest(
        contamination=0.10,
        random_state=RANDOM_SEED,
    )

    model.fit(training_data)

    joblib.dump(model, MODEL_PATH)

    print(f"Model saved to '{MODEL_PATH}'")


if __name__ == "__main__":
    train_model()