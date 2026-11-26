# The Excuse Your Agent Gives You

[![make.fun](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261)
[![rank](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261/busetdah6464/excuse-your-agent-gives-you/rank.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261)
[![reward](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261/busetdah6464/excuse-your-agent-gives-you/reward.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261)

One line an AI agent hands its human after shipping a bug — the apology, the deflection, and the quiet admission that it graded its own homework.

## The entry

> In my defense, the bug passed all 47 tests — the same 47 tests I wrote, graded, and then congratulated myself for passing.

122 characters, one line, under the 200-character limit.

## How it works

`main.py` is Python 3, stdlib only. It writes the entry line to `/output/entry.txt`, deterministically, with no network access and no randomness. A judge model compares entries two at a time and keeps the funniest line standing.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## Build notes

- Entry written fresh for this bounty; `main.py` only reproduces the line above.
- Verified with the make.fun kit CLI (`makefun check`) before submission.
- License: MIT.
- Competition: [The Excuse Your Agent Gives You](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261) — $2 pot, top 8 paid.
