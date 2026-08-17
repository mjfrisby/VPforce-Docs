# How Settings Work

TelemFFB separates **system settings** (how the application runs) from **aircraft settings** (how each aircraft feels). Understanding how aircraft settings are resolved makes the rest of the manual - and the Settings tab - much easier to follow.

## Where settings are stored

**System settings** are stored in the registry at:

- `HKEY_CURRENT_USER\Software\VPforce\TelemFFB`

Everything configured in the System→[System Settings](configuration.md) dialog lives here. Do not edit the registry manually — knowing the path helps when you migrate machines.

**Aircraft settings** are stored in the user appdata folder:

- `%LOCALAPPDATA%\VPForce-TelemFFB`

The user configuration file here holds only your changes. The full catalog of settings and their default values ships inside the application as a defaults file.

## The layers

When an aircraft loads, every setting is resolved through layers. The most specific layer that defines a value wins:

1. **Application defaults** - the bundled defaults file defines every available setting for every simulator and device type, with sensible baseline values.
2. **Class defaults** - defaults per aircraft class (PropellerAircraft, JetAircraft, TurbopropAircraft, GliderAircraft, Helicopter, and so on). A helicopter and a jet start from different baselines automatically.
3. **Shipped aircraft profiles** - TelemFFB ships tuned profiles for many specific aircraft across all supported sims. Aircraft are matched by a name pattern, so different liveries of the same aircraft match the same profile. The **Matched Model** field in the status area shows which pattern matched.
4. **Your overrides** - anything you change, at whatever level you choose: for the specific aircraft (the normal case), or promoted to apply class-wide or sim-wide.

Your configuration file is a **delta**: it stores only the settings you changed, at the level you changed them. Everything else continues to follow the layers below.

!!! tip "Why the delta model is good news"
    Because unmodified settings follow the application defaults, updating TelemFFB automatically picks up improved default values and newly added settings - without touching anything you tuned yourself. And any change you make can be reverted to the inherited value with one click, so experimenting is always safe.

## Reading the Settings tab

The Settings tab shows the *resolved* value of every setting for the loaded aircraft, whichever layer it came from. The interface tells you where a value comes from:

- A setting you changed for this aircraft shows an **x** icon. Click it to remove your override and fall back to the inherited value.
- **Right-click the x** icon to promote your value to the **class** or **sim** level, so it applies to every aircraft of that class or sim. An information icon then marks the setting; hover it to see which level the override lives at.

See [Modifying settings in real time](ui-overview.md#modifying-settings-in-real-time) for a visual walkthrough of these controls.

To edit class- or sim-level defaults directly - without an aircraft loaded - use the offline editor described in [Aircraft Profiles](aircraft-profiles.md#offlineglobal-simclass-configuration).

## Profiles

An aircraft can have more than one settings profile. The **Active Profile** field in the status area shows which one is loaded.

- Every aircraft has a base profile; you can create additional named profiles for the same aircraft - for example an aerobatics setup and a cruise setup - and switch between them.
- Profiles can be exported and imported for sharing.

Profile creation, selection, import and export are covered in [Aircraft Profiles](aircraft-profiles.md).

## Adding an aircraft that has no profile

If TelemFFB does not recognize a loaded aircraft, it still works: the aircraft gets the defaults for its simulator, and you can create a proper profile for it - choosing the aircraft class that determines its baseline - with the [Add New Aircraft wizard](aircraft-profiles.md#adding-new-aircraft-support). Picking the right class matters: it decides which spring model, effect set, and class defaults apply.
