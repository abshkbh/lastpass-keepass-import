I wrote this script to migrate from KeePassXC to LastPass. LastPass asked for
an XML file from KeePassX to do this migration. Unfortunately newer versions
of KeePassX only spit out a CSV.

This script converts a CSV spat out by KeePassX 1.43 to a CSV format
compatible with LastPass.

You can then go to "Import" in LastPass and choose "Generic CSV" as input. If
the importer fails then its likely your KeePassX CSV had some issues. It's easy
to hack on this little script.
