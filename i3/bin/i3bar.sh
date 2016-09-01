#!/bin/sh

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
I3_CONKY_CONFIG=$( dirname $DIR )'/i3conkyrc'

#send the header so that i3bar knows we are sending json
echo '{"version":1}'

#Begin the endless array.
echo '['

#Send and empty array first to make loop simpler
echo '[],'

#Send results from conky forever...
exec conky -c $I3_CONKY_CONFIG
