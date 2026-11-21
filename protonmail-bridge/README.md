# protonmail-bridge

Proton Mail Bridge for Neko-Void, built from source and linked against the
system Qt 6, gRPC, Protobuf and Sentry libraries.

## Build

Copy this directory into `srcpkgs/` of a void-packages checkout (or use vouru),
then:

```sh
./xbps-src pkg protonmail-bridge
sudo xbps-install --repository=hostdir/binpkgs protonmail-bridge
```

## Runtime

Bridge needs a freedesktop secret service for the account credentials:

```sh
sudo xbps-install gnome-keyring   # or: pass
```

`/usr/bin/protonmail-bridge` starts the GUI, `/usr/bin/protonmail-bridge-core`
starts the daemon/CLI. Bridge manages its own XDG autostart entry, so a runit
service is not required on a desktop install.

## Packaging notes

* Proton's signed launcher is not packaged: it is only usable with Proton's
  official release. The daemon is built from `cmd/Desktop-Bridge`.
* `files/system-deps.patch` adds the `BRIDGE_USE_SYSTEM_DEPS` CMake option and
  `files/protobuf-include.patch` passes Protobuf's include path to `protoc`.
  Both are skipped once the corresponding changes are part of a Bridge release.
* Update `version` and `checksum` together. The checksum is for
  `https://github.com/ProtonMail/proton-bridge/archive/refs/tags/v<version>.tar.gz`.

## Verification

The template was tested on a Void x86_64 glibc userland with Go 1.27.4, Qt
6.11.2, gRPC 1.83.0, Protobuf 35.1 and sentry-native 0.17.6: the daemon and GUI
built from the pristine v3.27.2 tarball plus the two patches, `bridge --version`
reported 3.27.2, the GUI started with `QT_QPA_PLATFORM=offscreen` and found the
daemon, and `protonmail-bridge-core --version` worked from the installed layout.
