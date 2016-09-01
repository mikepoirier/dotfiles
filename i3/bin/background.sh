#!/bin/sh

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
BACKGROUND=$DIR'/../resources/background'

feh --bg-scale $BACKGROUND
