#!/bin/bash
echo "Simple Interest Calculator"
echo "=========================="
read -p "Enter Principal: " p
read -p "Enter Rate: " r
read -p "Enter Time: " t
si=$(echo "scale=2; ($p * $r * $t) / 100" | bc)
echo "Simple Interest: $si"
