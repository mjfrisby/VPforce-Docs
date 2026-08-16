# VPforce TelemFFB Application

TelemFFB is an open source community-driven Python/Qt based application which takes telemetry from a simulator and uses that telemetry to produce various effects.

The latest version can always be downloaded from the [GitHub releases page](https://github.com/walmis/VPforce-TelemFFB/releases).

Supported simulators:

- DCS World
- Microsoft Flight Simulator
- IL-2 Sturmovik
- X-Plane 11/12
- Beta support for Falcon BMS (4.38+)

For **DCS** and **IL-2**, which support native FFB, the TelemFFB app is primarily leveraged to implement certain effects like gunfire, engine rumble and helicopter ETL shaking (among many others). However, there are some additional 'FFB type' effects which are implemented such as deceleration force and g-loading effect.

For **MSFS** and **X-Plane**, which ***do not*** have native FFB support, TelemFFB also implements dynamic axis FFB in addition to most of the effects previously mentioned for DCS.

**Falcon BMS** sits somewhere in between. While the game does support native FFB with limited native effects, the primary F-16 aircraft is fly-by-wire and as such does not have any traditional "force feedback" on its flight stick. TelemFFB implements several haptic style effects (gunfire, buffeting, etc) to augment immersion.

## How it works

TelemFFB started out its life as not much more than a haptic effect generator driven by telemetry, originally only for DCS. It started out by adding supplemental effects such as engine rumble and gunfire on top of the native force feedback effects supported directly by the simulator.

It has grown since then into a highly configurable, feature rich application supporting not only supplemental haptic effects but also full dynamic FFB modeling for simulators such as Microsoft Flight Simulator (20/24) and X-Plane that do not have **any **native FFB support.

TelemFFB leverages telemetry that is available from a given simulator and uses that telemetry to create various types of effects based on real-time analysis of said telemetry.

In practice, it is more complicated and depends largely on the simulator. However, it can be mostly broken down into two categories: Simulators ***with ***native FFB support and those ***without***.

**Sims with native FFB**

- This includes **DCS**, **IL-2** and, to some extent, **BMS**. For these simulators, TelemFFB is primarily a haptics and supplemental effects generator. While there are overrides that a user can implement to use TelemFFB to manage the dynamic spring effect, the native game-supplied spring effect is typically used most of the time. This means that the game is managing the spring effect, while TelemFFB would be adding additional effects on top.

- For these simulators, by default, the spring effect, including trim/autopilot following is managed wholly by the game itself.

**Sims without native FFB**

- This includes both **Microsoft Flight Simulator** as well as **X-Plane**. Fortunately both of these titles have much more rich telemetry than the others and have sufficient data to implement not just simple speed based dynamic spring, but spring loading that is based on calculated dynamic pressure throughout the aircraft speed envelope as defined by the telemetry data.
- For these simulators, the **entire** FFB implementation is handled by the TelemFFB application

For a detailed look at how native simulator FFB, TelemFFB, and VPforce Configurator device settings interact, see [Understanding Native DCS FFB, TelemFFB, and VPforce Configurator](sim-dcs.md#understanding-native-dcs-ffb-telemffb-and-vpforce-configurator) in the DCS guide.
