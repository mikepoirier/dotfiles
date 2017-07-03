#!/bin/bash

pac=$(checkupdates | wc -l)
aur=$(pacaur -Qu | wc -l)

echo " $pac / $aur"
