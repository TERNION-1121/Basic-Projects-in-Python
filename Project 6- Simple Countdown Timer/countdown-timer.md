# Countdown Timer ⏲
This program serves as a simple countdown timer (`countdown()`), which takes an argument `t` _(where **t** is the time in seconds)_. 
It has two functions defined :-
1. **annoy()**
2. **countdown()**
<hr>

### `annoy()`
This function makes use of the `Beep()` function in the module **winsound**, inside a *for* loop to produce a beeping sound. That would be further needed when the timer goes 0.

### `countdown()`
This function prints the time after the delay of **1 second**, and as soon as the timer hits 0, the `annoy()` function is called.

```py
while t >= 0:
        min, sec = divmod(t, 60)
        print(f"{min:.2f} : {sec:.2f}", end = '\r')
        time.sleep(1)
        t -=1
    annoy()
    print("Time Up!    ")
```
