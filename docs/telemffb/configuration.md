# System Settings

In the System Menu, choose System Settings:
![](../rhino/media/Pictures/10000000000002860000026C339E3AB987AF6F65.png){ width="549px" height="527px" }

!!! note
    For where these settings are stored on disk, see [How Settings Work](settings-model.md). The **Launch Options** page is covered in [Devices & Instances](devices-instances.md), and the **Sim Setup** page in [Connecting Your Simulator](sim-setup.md).

## System Page

### System

These settings are unique per device instance of TelemFFB

-   **System Logging Level**

    -   Control the logging level for an instance of TelemFFB

-   **Telemetry Timeout**

    -   Control the telemetry timeout value for an instance of TelemFFB

-   **Update Prompt Control**

    -   Enable/Disable the new-update prompt for an instance of TelemFFB when starting up.

-   **Prune Logs**

    -   Enable log pruning. Archived log zip files that are older than the configured threshold will be automatically deleted upon TelemFFB startup.

### Theme Options

!!! note
    The Theme Options are global and are only visible in the Master instance of TelemFFB

-   **Light** - Use the light color palette theme
-   **Dark**- Use the dark color palette theme
-   **System** (default) - Use the Windows system defined app theme dark/light mode

## Startup Behavior Page

### Startup Behavior

-   **Start with Windows (Global, Master Only)**

    -   When enabled, an entry will be added to the Windows registry
        that will start TelemFFB automatically when Windows starts

    !!! note
        Only available with the EXE distribution of TelemFFB. This option will be disabled when running from source.

-   **Start in System Tray (Global, Master Only)**

    -   When enabled, TelemFFB will start up minimized to the system
        tray. The main window can be recalled by double-clicking the
        system tray icon or from the right-click context menu on the
        system tray icon.

    !!! note
        This is mutually exclusive with the Start Minimized option. Only one or the other may be enabled.

-   **Start Minimized (Global, Master Only)**

    -   When enabled, TelemFFB will start with its main window visible,
        but minimized to the taskbar.

    !!! note
        This is mutually exclusive with the Start in System Tray option. Only one or the other may be enabled.

-   **Closing App Sends to Tray (Global, Master Only)**

    -   When enabled, pressing the window close button will simply
        minimize the application to the system tray.

    -   You can fully exit TelemFFB from the System menu or from the
        right-click context menu on the system tray icon.

These settings are unique per instance of TelemFFB

-   **Restore Window Position**

    -   When enabled, TelemFFB will remember where the window was positioned the last time it was run and restore the window to that same position

-   **Restore Last Tab View**

    -   When enabled, TelemFFB will remember the window size for each tab the last time it was run. It will also restore these sizes and remember the last tab that was viewed the last time it was run.

### Configurator Profile Options

-   **VPForce Configurator Profiles**

    -   Define a profile to load on TelemFFB startup and/or exit

    -   See the section on ***Dynamic Configurator Profiles*** for more details
