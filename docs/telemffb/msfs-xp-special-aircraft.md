# Aircraft with Special Treatment

Several addon aircraft receive treatment beyond the standard aircraft classes. This takes one or more of three forms:

- A **dedicated aircraft class** - a deeper integration written specifically for that aircraft's systems (AFCS following, cockpit control locks, flight-model vibration data).
- **Class or profile defaults** tailored to the aircraft - spring modes, force trim, or non-standard axis variables pre-configured to match how the addon works.
- **[Telemetry overrides](telem-overrides.md)** in the shipped default profile - telemetry items re-sourced from the addon's custom variables, or additional items subscribed.

!!! important "Additional profiles for these aircraft: clone, don't create from scratch"
    Everything on this page is carried by the aircraft's shipped default profile - the class assignment, the curated settings, and any telemetry overrides. If you need an additional profile (a livery whose name does not match the default pattern, for example), you must **clone it from the default profile**. A profile created from scratch will not carry the special treatment, and the integration silently stops working. See [Aircraft Profiles](aircraft-profiles.md) for cloning.

| Aircraft | Sim | Class |
|---|---|---|
| [HPG Airbus H145 / H160](#hpg-airbus-h145-h160) | MSFS | `HPGHelicopter` |
| [FlyInside B206 / B47](#flyinside-b206-b47) | MSFS | `FlyInsideHelicopter` |
| [CowanSim fleet](#cowansim-helicopters) (10 models) | MSFS | `CowanSimHelicopter` |
| [Taog's Hangar H500C / OH6A](#taogs-hangar-h500c-oh6a) | MSFS | `TaogH500Helicopter` |
| [Taog's Hangar UH-1H / Bell 205-A1B](#taogs-hangar-uh-1h-bell-205-a1b) | MSFS | `Helicopter` (standard) |
| [Simfocus Bell 407](#simfocus-bell-407) | MSFS | `SASHelicopter` |
| [A2A Comanche (PA-24)](#a2a-comanche-pa-24) | MSFS | `PropellerAircraft` (standard) |
| [X-Trident AW109SP](#x-trident-aw109sp) | X-Plane | `XAW109Helicopter` |

## HPG Airbus H145 / H160

The deepest integration in TelemFFB, developed in collaboration with HPG: the stick works with the AFCS as the real auto-trim motor does, with force trim release, hands-on detection, and collective/pedal integration. The default profiles subscribe to a set of HPG SDK `L:Var`s (SEMA positions, AFCS state, trim release, hands-on) via telemetry overrides, and the class defaults set Hardware Force Trim spring mode on all axes.

Full setup requirements and settings are covered in [HPG Airbus Helicopters](msfs-xp-helicopters.md#hpg-airbus-helicopters-msfs-only).

## FlyInside B206 / B47

Developed in collaboration with FlyInside: instead of TelemFFB's synthesized buffeting and rumble, **vibration channels from the FlyInside flight model** drive the effects directly (the *Vibration* control under Mechanical/Airframe). The default profiles re-source the engine and rotor RPM (and, on the B206, the hydraulics state) from FlyInside's own variables, and the class defaults use the No Spring mode on all axes.

See [FlyInside Helicopters](msfs-xp-helicopters.md#flyinside-helicopters-msfs-only).

## CowanSim Helicopters

The entire CowanSim fleet has default profiles with the `CowanSimHelicopter` class: **206B3, 206L3, 222B, 222UT, 500E, H125, H130, R22, R66, and S-76C++**. (The H125 match pattern deliberately excludes the stock Asobo H125 variants.)

What's different: with Axis Control enabled, the cyclic positions are sent through **CowanSim's own axis variables** (`L:COWANSIM_CYCLIC_X_POSITION` / `L:COWANSIM_CYCLIC_Y_POSITION`) rather than the standard cyclic events, pre-configured via the Custom Axis Variables feature in the class defaults. The R66 profile additionally re-sources the hydraulic-switch telemetry from CowanSim's custom variable.

## Taog's Hangar H500C / OH6A

The `TaogH500Helicopter` class honors the aircraft's **cockpit control locks**: engaging the cyclic or collective friction lock (or the pedal lock) stops TelemFFB's axis-position sends for that control, so the locked control stays put in the sim no matter how the physical axis moves. Tail-rotor damage in the flight model also cuts pedal control. The lock states arrive via telemetry overrides on Taog's `L:Var`s, and the class defaults use the No Spring mode on all axes.

## Taog's Hangar UH-1H / Bell 205-A1B

These use the standard `Helicopter` class, but the default profiles wire the cockpit **force-trim switch** (`L:switchForceTrim`) to the [Force Trim Switch Simvar](msfs-xp-helicopters.md#helicopter-force-trim) feature - hardware force trim engages and disengages with the switch in the cockpit, as in the real aircraft.

## Simfocus Bell 407

The `SASHelicopter` class provides an SAS/AFCS integration in the HPG style: the stick slowly follows the SEMA actuator positions (subscribed via telemetry overrides), with hands-on detection so the AFCS yields while you fly. The class defaults set Hardware Force Trim on the cyclic and disable ordinary trim following - the AFCS integration moves the stick instead. Requires Axis Control with the cyclic axes unbound in MSFS.

## A2A Comanche (PA-24)

A standard `PropellerAircraft` - the special treatment is entirely in the default profile's telemetry overrides, which re-source the autopilot state, prop RPM, prop thrust, and body accelerations from A2A's Accu-Sim variables (the standard simvars read stale on this aircraft). This is the [worked example](telem-overrides.md#reading-the-example) on the Telemetry Overrides page.

## X-Trident AW109SP

An X-Plane implementation via the `XAW109Helicopter` class, developed with input from the aircraft's developer: 4-axis AFCS integration (cyclic trim-rate control, force trim release, autopilot following), pedals that actively track the anti-torque requirement as power and airspeed change (a TelemFFB-side model of the parallel trim actuator, compensating for the limited yaw-servo telemetry the aircraft exports), and collective spring gain with force trim release - driven by a large set of AW109 datarefs subscribed through telemetry overrides. The class defaults set Hardware Force Trim spring mode on all axes.

Full setup requirements - including the aircraft's own Configurations page settings, which must match the integration - are covered in [X-Trident AW109](msfs-xp-helicopters.md#x-trident-aw109-x-plane-only).

!!! warning "Known issue"
    The aircraft does not honor the axis-override dataref nor properly accept external axis control - **map your controls in-game and leave Axis Control disabled in TelemFFB** (the default profile ships with it disabled).
