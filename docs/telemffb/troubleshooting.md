# Troubleshooting & Getting Help

Most real-world problems are simulator connection issues, and the detailed checklists for those live in [Game-Specific Troubleshooting](../rhino/game-specific-troubleshooting.md). This page is the map: how to tell what kind of problem you have, where the diagnostics are, and how to get help.

## Read the status area first

The main window's status area narrows the problem immediately:

-   **Running** — the sim is connected and telemetry is flowing. If something feels wrong, it is configuration, not connectivity — check the loaded settings via **Current Aircraft**, **Matched Model**, and **Active Profile**.
-   **Paused** — telemetry stopped arriving, or the sim is paused.
-   **Error** — a configuration problem. The error message shown alongside describes the condition and how to resolve it.

See [Device/Instance Status Indications](ui-overview.md#deviceinstance-status-indications) for details. The **Monitor tab** shows the raw telemetry and every active effect in real time — useful for confirming what TelemFFB is actually receiving and playing.

## Simulator connection problems

Verify the sim is enabled in [Connecting Your Simulator](sim-setup.md), then use the detailed per-sim checklists:

-   **DCS** — [FFB not working](../rhino/game-specific-troubleshooting.md#ffb-not-working) · [Not receiving telemetry](../rhino/game-specific-troubleshooting.md#not-receiving-telemetry) · [Autopilot misbehaving](../rhino/game-specific-troubleshooting.md#autopilot-misbehaving-or-disengaging-unexpectedly)
-   **MSFS** — [Axis flutter / controls not responding](../rhino/game-specific-troubleshooting.md#controls-not-responding-correctly-axis-flutter) · [A feature doesn't work with a specific aircraft](../rhino/game-specific-troubleshooting.md#a-feature-doesnt-work-with-a-specific-aircraft)
-   **IL-2** — [Not receiving telemetry](../rhino/game-specific-troubleshooting.md#not-receiving-telemetry_1)
-   **X-Plane** — [Not receiving telemetry](../rhino/game-specific-troubleshooting.md#not-receiving-telemetry_2)
-   **BMS** — [Falcon BMS](../rhino/game-specific-troubleshooting.md#falcon-bms)

## Getting help

The single most important factor in getting your problem solved quickly is **how you ask**. Read **[How to Get Effective Support](../rhino/troubleshooting-maintenance.md#how-to-get-effective-support)** — it is short, and following it usually turns a multi-day back-and-forth into a single exchange. The essentials:

-   **Describe exactly what happens and when** — "stick goes limp with no centering force in the F-16 after AP engage", not "FFB doesn't work". One problem per request, and say what you have already tried.
-   **Include VPforce Configurator screenshots** — Effects, Settings, and Debug tabs. Without them, diagnosis is guesswork.
-   **Attach a TelemFFB support bundle**: **Help → Create Support Bundle** produces a timestamped zip of your logs, system settings, and user config — it usually contains everything needed for diagnosis.
-   Post on the **[#TelemFFB-User](https://discord.com/channels/965234441511383080/968208779084701716)** channel of the VPforce Discord.

For reference: **System → Open Config/Log directory** opens the folder holding logs and your settings (`%LOCALAPPDATA%\VPForce-TelemFFB`); older logs are archived into daily zip files.

## FAQ

**Q: Does DCS native force feedback need TelemFFB running?**  
**A:** No. DCS sends its native FFB effects directly to the device. TelemFFB adds supplemental effects on top — see [the DCS guide](sim-dcs.md#understanding-native-dcs-ffb-telemffb-and-vpforce-configurator).

**Q: My antivirus flags the TelemFFB executable. Is it safe?**  
**A:** This is a known false-positive pattern with PyInstaller-packaged applications. See [TelemFFB and Antivirus Software](installation.md#telemffb-and-antivirus-software).

**Q: How do I update TelemFFB without losing my settings?**  
**A:** Extract the new version over (or beside) the old one. Your settings live in `%LOCALAPPDATA%\VPForce-TelemFFB` and the registry, not in the application folder, so they survive updates.

**Q: Running from source and the release build — separate settings?**  
**A:** No, they share the same configuration. Changes made in one carry over to the other.
