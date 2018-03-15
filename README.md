## Kodi Controller
Full-featured controller for Kodi instances on the local network

## Description 
The Kodi Controller Skill allows Mycroft to control Kodi, whether locally installed
or on another device on the local network.  It will allow a high degree of control
over Kodi, including the ability for the user to specify a device IP for the Kodi
player (allowing the skill to control Kodi on multiple different devices without
requiring the user to manually edit the skill's settings), to search for videos and
music, and to control playback.

## Examples 
* "Connect to Kodi at &lt;IP address&gt;"
* "Pause Kodi"
* "Pause playback in Kodi"
* "Resume Kodi"
* "Resume playback in Kodi"
* "Stop Kodi"
* "Stop playback in Kodi"
* "Enable subtitles in Kodi"
* "Disable subtitles in Kodi"
* "Search Kodi for <title>"

## Credits 
Matt Burns

## Notes
While three other skills for Kodi are already available for Mycroft, none are in
active development, none provide the degree of control this skill intends to
provide, and none allow an easy way to switch between different devices.

The Kodi Controller Skill uses Kodi's JSON-RPC API, and requires the kodipydent
Python module.

## Setup

In Kodi, enable "[Allow remote control via HTTP](https://kodi.wiki/view/Settings/Services/Control)".  

Enter the connection information in the Skills settings page of Mycroft Home.  Eventually, the user will be able to connect to Kodi (if using the default port with no password) using the device's IP address using any of the following commands:
"Mycroft, connect to Kodi on &lt;IP address&gt;"
"Mycroft, connect to Kodi at &lt;IP address&gt;"
"Mycroft, Kodi connect &lt;IP address&gt;"

## Usage

### Connection

* Connect: "Connect to Kodi on &lt;IP address&gt;", "Connect to Kodi at &lt;IP address&gt;", "Kodi connect &lt;IP address&gt;"  **&#91;WIP&#93;** 

### Input Controls

* Up: "Kodi up"
* Down: "Kodi down"
* Left: "Kodi left"
* Right: "Kodi right"
* Select: "Kodi select", "Kodi click", "Kodi enter"
* Info: "Kodi info"
* Home: "Kodi home"
* Context menu: "Kodi context"
* Back: "Kodi back"

### Playback

* Pause: "Kodi pause", "Kodi pause playback", "Pause Kodi", "Pause playback in Kodi"
* Play: "Kodi play", "Play Kodi", "Kodi unpause", "Unpause Kodi"
* Stop: "Kodi stop", "Kodi stop playback", "Stop Kodi"
* Resume/rewatch last played: "Kodi resume", "Kodi resume playback", "Resume playback in Kodi", "Kodi play last watched" **&#91;WIP&#93;** 
* Seek forward: "Kodi skip ahead", "Kodi seek forward"
* Seek backward: "Kodi skip back", "Kodi seek backward"
* Show on-screen display: "Kodi display", "Kodi show on-screen display"
* Search/open media: "Kodi find &lt;title&gt;", "Kodi search for &lt;title&gt;", "Search Kodi for &lt;title&gt;", "Search in Kodi for &lt;title&gt;"  **&#91;WIP&#93;** 
* Play random movie: "Kodi play a random movie", "Play a random movie in Kodi", "Kodi random movie" **&#91;WIP&#93;** 
* Enable subtitles: "Kodi enable subtitles", "Enable subtitles in Kodi", "Kodi turn on subtitiles" **&#91;WIP&#93;** 
* Disable subtitles: "Kodi disable subtitles", "Disable subtitles in Kodi", "Kodi turn off subtitles" **&#91;WIP&#93;** 

### Media Library

* Scan for new video: "Kodi scan movies", "Kodi scan videos"
* Scan for new audio: "Kodi scan audio"

## TODO

* Fix ability to enable/disable subtitles
* Add ability to search for and play movies
* Add ability to play a random movie
* Add ability to play last watched video
