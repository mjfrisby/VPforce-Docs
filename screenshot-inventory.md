# TelemFFB Screenshot Review Checklist

All legacy images are renamed into `docs/telemffb/images/<page>/<name>` and
the pages reference the new paths. To update a stale capture, **overwrite the
file with the same name** — no page edits needed. Check items off as reviewed.
Not site content; delete this file when done.

## aircraft-profiles

- [ ] `export-dialog.png`
- [ ] `import-1.png`
- [ ] `import-2.png`
- [ ] `import-3.png`
- [ ] `import-4.png`
- [ ] `new-aircraft-main.png`
- [ ] `offline-editor.png`
- [ ] `profile-manager-context.png`
- [ ] `profile-manager.png`
- [ ] `wizard-1.png`
- [ ] `wizard-2.png`

## configuration

- [ ] `system-settings.png`

## devices-instances

- [ ] `launch-options.png`

## effects-inertial

- [ ] `gforce-curvature-plot.png`

## installation

- [ ] `first-launch.png`

## msfs-xp-axis-spring

- [ ] `dynamic-settings.png`
- [ ] `expo-curve.png`
- [ ] `fbw-gains.png`
- [ ] `spring-centered.png`
- [ ] `spring-mode-select.png`

## msfs-xp-helicopters

- [ ] `collective-spring-mode.png`
- [ ] `configurator-adaptive-recentering.png`
- [ ] `flyinside-vibration.png`
- [ ] `force-mode.png`
- [ ] `force-trim-settings.png`
- [ ] `hpg-guide-excerpt.png`
- [ ] `hpg-tablet.png`

## msfs-xp-trim-following

- [ ] `ap-following-settings.png`
- [ ] `calibration_dialog.png`
- [ ] `calibration_in_progress.png`
- [ ] `example_calibration.png`
- [ ] `settings.png`

## sim-dcs

- [ ] `dcs-spring-override.png`

## sim-il2

- [ ] `il2-input-shaking.png`
- [ ] `il2-shake-master.png`

## spring-curves

- [ ] `adv-spring-curve.gif`  *(GIF)*
- [ ] `adv-spring-dialog.png`
- [ ] `adv-spring-entry.png`
- [ ] `adv-spring-smooth.gif`  *(GIF)*
- [ ] `gforce-curve-dialog.png`
- [ ] `gforce-curve-example.png`

## ui-overview

- [ ] `active-devices.png`
- [ ] `button-capture.gif`  *(GIF)*
- [ ] `device-switching.gif`  *(GIF)*
- [ ] `expander.gif`  *(GIF)*
- [ ] `hide-tab.png`
- [ ] `main-window.png`
- [ ] `monitor-tab.png`
- [ ] `promote-override.gif`  *(GIF)*
- [ ] `revert-x.gif`  *(GIF)*
- [ ] `settings-tab.png`
- [ ] `slider-toggle.png`
- [ ] `status-area.png`
- [ ] `status-error.png`
- [ ] `status-paused.png`
- [ ] `status-running.png`
- [ ] `system-tray.png`
- [ ] `tray-menu.png`
- [ ] `tray-status-error.png`
- [ ] `tray-status-paused.png`
- [ ] `tray-status-running.png`
- [ ] `unit-dropdown.png`

## vpconf-profiles

- [ ] `aircraft-vpconf.png`
- [ ] `gain-overrides.png`
- [ ] `startup-exit-profiles.png`


## New captures needed - dinput branch (ALL CAPTURED 2026-08-27 and wired into the pages)

Placeholders are in the pages as commented-out image tags marked
`TODO screenshot` - capture the image, drop it at the listed path, and
uncomment the tag.

### dinput-tap

- [x] `tap-section.png` - System Settings, a sim tab (DCS suggested) with the DirectInput Tap toggle ON and the status panel showing an installed wrapper (version and config rows visible)
- [x] `device-dialog.png` - the tap device-capture dialog with a device or two checked
- [x] `spring-mode.png` - the Settings tab spring-mode dropdown open, showing "Game Managed (DirectInput Tap)"
- [x] `tap-settings.png` - the Settings tab with "Tap: Axis Corrections and Gain" and "Tap: Additional Game Effects" groups expanded
- [x] `effects-monitor.png` - the effects monitor in flight showing "Game Spring (DirectInput Tap)" and at least one other Game effect active
- [x] `update-offer.png`
- [x] `update-offer_sim-settings.png` - follow-on: the tap status panel flagging an out-of-date copy (added during capture)
- [x] `another-dll.png` - follow-on: the panel and cautious replace prompt for an UNRECOGNIZED dinput8.dll (added during capture)
- [x] `ffbfix-dll.png` - follow-on: the panel and affirmative upgrade prompt for a RECOGNIZED ffb-fix wrapper (added after the LEGACY-detection feature)
- [x] `diff-preview.png` - follow-on: Configure Devices -> Preview -> proposed-changes diff progression, with arrows (added during capture) - the startup "DirectInput Tap Updates" prompt (requires an older wrapper installed in a sim folder)

### devices-instances

- [x] `joystick-alternates.png` - Launch Options with the joystick card holding two or three devices: primary radio marker, per-row icons, "+ add device" visible
- [x] `aircraft-device.png` - an aircraft's Settings tab showing the Device section with the Joystick Device selector open ("Primary (default)" plus named devices, the `*` marker visible)

### configuration

- [x] `system-settings.png` - RECAPTURE existing shot: the dialog is reorganized into Devices / System / Simulator Setup tabs; capture it open on the System tab (includes the "Enable DirectInput Devices" toggle)

### devices-instances (reorganized dialog)

- [x] `devices-tab.png` (captured as device-settngs.png, renamed) - the full Devices tab: device cards (selectors, master marker, auto-launch and minimized/headless switches) with the Device Settings area visible below. ONE capture, used by both Devices & Instances and System Settings (replaces the retired `launch-options.png` - the Launch Options page no longer exists)

### sim-setup

- [x] `simulator-setup.png` - RECAPTURE existing shot: now the Simulator Setup tab with per-sim pages (and the DirectInput Tap sections on DCS/IL-2/BMS)

### installation

- [x] `first-launch.png` - RECAPTURE
- [x] `first-launch_notify.png` - follow-on: the first-launch auto-assignment notice (added during capture, shown in Quick Start) existing shot: the first-launch System Settings dialog with the new tab layout
