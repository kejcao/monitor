#!/bin/bash

sleep 5

evtest /dev/input/by-id/usb-04d9_USB_Keyboard-event-kbd \
	| stdbuf -o0 grep -o '(KEY_.*), value 1' \
	| stdbuf -o0 sed 's/^(\(.*\)).*$/\1/g' \
	| python3 keyboard.py &

evtest /dev/input/by-id/usb-17ef_Lenovo_Optical_Mouse-event-mouse \
	| stdbuf -o0 grep -o '(BTN_.*), value 1\|(REL_.*), value .*\|SYN_REPORT' \
	| stdbuf -o0 sed 's/^(\(REL_.*\)), value \(.*\)/\1 \2/; s/^(\(.*\)).*$/\1/g' \
	| python3 mouse.py
