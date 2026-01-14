# energywar

How much energy does AI use compared to gaming?

This tool compares the estimated energy use of active players on Steam over 24 hours to the largest estimate I was able to find for the energy use required to train GPT-4 (62,318,750 kWh). Training is used as the benchmark for LLM energy usage because training is massively higher than inference energy usage [^1] [^2].

Estimates are biased in favor of gaming (lower is better) by introducing an estimate that only 50% of Steam's concurrently logged-in users are actively playing a game _and_ estimating that the average energy use for a gaming PC is 0.2 kWh per hour, 30% below the estimate for mid-range gaming PCs in 2025 [^3].

## Output

```
Steam games (24h): 69,611,999 kWh
GPT-4 training   : 62,318,750 kWh
Ratio            :       1.117031
```

## Assumptions

- Use a 24-hour, time-weighted average of Steam's concurrent logged-in users from `userdata.json`.
- Assume 50% of those users are actively playing.
- Assign 0.2 kWh per hour (~0.2 kW) of GPU energy per active player.
- Multiply the per-hour energy by 24 to estimate a daily total in kWh.
- Compare against 62,318,750 kWh as a high-end estimate for GPT-4 training energy.

If the 50% estimate for active players is too large, divide the total energy use by 10 to get 5%, and then multiply by 10 days to get back to the original answer.

The data sources do not account for console gaming, mobile gaming, or non-steam PC gaming. The energy estimate for gaming PCs only accounts for GPU energy, not the rest of the computer, network equipment, or servers.

## Conclusion

Training a large language model requires approximately the same amount of energy as all GPUs on Steam use over the course of 1 to 10 days.

## Data sources:

- https://www.technologyreview.com/2025/05/20/1116327/ai-energy-usage-climate-footprint-big-tech/
- https://towardsdatascience.com/the-carbon-footprint-of-gpt-4-d6c676eb21ae/
- https://store.steampowered.com/stats/userdata.json
- https://store.steampowered.com/hwsurvey
- https://www.techpowerup.com/review/msi-geforce-rtx-4060-gaming-x/39.html
- https://www.techpowerup.com/review/zotac-geforce-rtx-5060-solo-8-gb/39.html
- https://www.techpowerup.com/gpu-specs/geforce-rtx-4060-mobile.c3946

[^1]: https://arxiv.org/html/2412.00329v1
[^2]: https://arxiv.org/html/2407.16893v1
[^3]: https://solartechonline.com/blog/how-much-electricity-does-gaming-pc-use/
