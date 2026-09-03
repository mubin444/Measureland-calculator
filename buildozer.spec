[app]

# (str) Title of your application
title = Precision Land Calculator

# (str) Package name
package.name = land calculator juel

# (str) Package domain
package.domain = org.landcalc

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 1.0.0

# (list) Application requirements
requirements = python3,kivy==2.3.0

# (str) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (int) Target Android API
android.api = 33

# (int) Minimum API required
android.minapi = 21

# (int) Android NDK version
android.ndk = 25b

# (bool) If True, automatically accept NDK license
android.accept_sdk_license = True

# (str) Android archs to build for
android.archs = arm64-v8a, armeabi-v7a

[buildozer]

# (int) Log level
log_level = 2

# (str) Path to build artifact storage
warn_on_root = 1
