# Type
## Python
> Date/Time is represented as Float
> Precision depends on clock(system clock/monotonic clock/performance counter/process time)

### clock
> each has different precision and different starting point
> from hardware(impulses at different freqs) like clock generator, RTC(lives on battery), NTP(for synchronizing purpose)
> perf_counter, monotonic, process_time, clock, time