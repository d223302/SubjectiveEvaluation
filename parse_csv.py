#!/usr/bin/env python3
import numpy as np
import pandas as pd
import argparse
from collections import defaultdict
import statsmodels.stats.api as sms


parser = argparse.ArgumentParser()
parser.add_argument("--input")
args = parser.parse_args()

raw_result = pd.read_csv(args.input, dtype = str, keep_default_na=False, na_values=['_'])
raw_result.reset_index()
print("| Title | Platform | Qualification | Post-filter | Language background | Location | # of raters and rated items | Payment | Instructions | Increment (MOS)|")

print("| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")

for idx, response in raw_result.iterrows():
  output = []
  output.append(response["Title"])

  if "amt" in response["Plateform"].lower():
    output.append("Mturk")
  elif "prolific" in response["Plateform"].lower():
    output.append("Prolific")
  elif "uhrs" in response["Plateform"].lower():
    output.append("UHRS")
  else:
    output.append("x")

  if response["Qualification"].strip().lower() == "n/a":
    output.append("x")
  else:
    output.append("v")

  if response["Postprocessing"].strip().lower() == "n/a":
    output.append("x")
  else:
    output.append("v")

  if response["Linguistic background"].strip().lower() == "n/a":
    output.append("x")
  else:
    output.append("v")

  if response["Geographic location"].strip().lower() == "n/a":
    output.append("x")
  else:
    output.append("v")


  flag = 0
  for x in ["# of total rater", "rater per wav", "wav per rater", "Number of .wav"]:
    if response[x].strip().lower() != "n/a":
      flag += 1
  if flag == 0:
    output.append("x")
  elif flag == 4:
    output.append("v")
  else:
    output.append("△")

  if response["payment"].strip().lower() == "n/a":
    output.append("x")
  else:
    output.append("v")

  if response["Instruction"].strip().lower() == "n/a":
    output.append("x")
  else:
    output.append("v")

  if response["Increment"].strip().lower() == "n/a":
    output.append("x")
  elif "not" in response["Increment"].strip().lower():
    output.append("-")
  else:
    output.append(response["Increment"])


  output = "|" + " | ".join(output) + "|"

  print(output)
