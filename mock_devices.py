"""
Mock Mobile SDK

In a real application these values would come from a mobile SDK.

For this showcase we simply expose several representative device profiles
that can be used to demonstrate anomaly detection.
"""

from copy import deepcopy


# ---------------------------------------------------------------------------
# Device Profiles
# ---------------------------------------------------------------------------

SAFE_DEVICE = {
    "os_version": 14,
    "network": "private_wifi",
    "vpn_enabled": True,
    "developer_mode": False,
    "rooted": False,
    "bootloader_unlocked": False,
    "screen_lock": True,
    "play_protect": True,
    "usb_debugging": False,
    "unknown_sources": False,
}


PUBLIC_WIFI_DEVICE = {
    "os_version": 13,
    "network": "public_wifi",
    "vpn_enabled": False,
    "developer_mode": False,
    "rooted": False,
    "bootloader_unlocked": False,
    "screen_lock": True,
    "play_protect": True,
    "usb_debugging": False,
    "unknown_sources": False,
}


DEVELOPER_DEVICE = {
    "os_version": 13,
    "network": "private_wifi",
    "vpn_enabled": False,
    "developer_mode": True,
    "rooted": False,
    "bootloader_unlocked": False,
    "screen_lock": True,
    "play_protect": False,
    "usb_debugging": True,
    "unknown_sources": True,
}


ROOTED_DEVICE = {
    "os_version": 11,
    "network": "public_wifi",
    "vpn_enabled": False,
    "developer_mode": True,
    "rooted": True,
    "bootloader_unlocked": True,
    "screen_lock": False,
    "play_protect": False,
    "usb_debugging": True,
    "unknown_sources": True,
}


DEVICE_PROFILES = {
    "safe": SAFE_DEVICE,
    "public_wifi": PUBLIC_WIFI_DEVICE,
    "developer": DEVELOPER_DEVICE,
    "rooted": ROOTED_DEVICE,
}


def get_device(profile: str) -> dict:
    """
    Return a copy of the requested mock device.

    Returning a deepcopy prevents callers from accidentally modifying
    the original profile.
    """
    if profile not in DEVICE_PROFILES:
        raise ValueError(f"Unknown device profile: {profile}")

    return deepcopy(DEVICE_PROFILES[profile])