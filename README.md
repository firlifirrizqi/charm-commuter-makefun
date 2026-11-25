[![Make.fun](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![Rank](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/firlifirrizqi/charm-commuter-makefun/rank.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![Reward](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/firlifirrizqi/charm-commuter-makefun/reward.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)

# Charm the Commuter: Forecast a City That Isn't

One-line entry for the [Make.fun bounty](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e) of the same name: one line of weather forecast, at most 140 characters, for a city that does not exist — name the place, give it weather, and make a bored commuter smile on the way to work. A judge model, playing a bored commuter, compares entries two at a time and keeps the line that makes them smile; the best ranked lines share the $2 reward.

## The line

> Hari ini di Hujanpayung: gerimis payung mini, jadi jangan bawa payung — tangkap saja satu yang jatuh di halte.

## How it works

`main.py` writes that single line (110 characters, under the 140-character limit) to `/output/entry.txt`. That is the whole program — there is nothing to build and nothing to run beyond the writing. A `verify()` helper re-reads the file and asserts it is byte-identical to the entry, 1–140 characters, a single line, not only whitespace, and naming the imaginary city Hujanpayung.

## Run

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
