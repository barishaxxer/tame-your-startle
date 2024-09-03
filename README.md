# tame-your-startle
> [!CAUTION]
> Long or repeated exposure to sounds at or above 85 dBA can cause hearing loss.[^1]

> [!TIP]
> The acoustic startle response is reliably elicited by bursts of noise or tones having sound pressure levels (SPLs; re 20 μPa) of 80–90 dB and greater.[^2]

Train your startle reflex while doing your spreadsheets!
#### Video Demo: <>
#### Description:
In animals, including humans, the startle response is a largely unconscious defensive response to sudden or threatening stimuli, such as sudden noise or sharp movement, and is associated with negative affect.[^3] The startle reflex is a brainstem reflectory reaction (reflex) that serves to protect vulnerable parts, such as the back of the neck (whole-body startle) and the eyes (eyeblink) and facilitates escape from sudden stimuli.Although startle reflex is protective,its unnecessary for most in modern age.Some people tend to give strong reactions to unexpected events and overreacting can be annoying sometimes!Tame your startle project aims to help people who are overreactive to control their startle response.
#### Installation
```bash
pip install -r requirements.txt
```
That's it!

#### Usage:
Create sound waves
> -w stands for db and -d stands for duration of sound(also --wave and --duration)
```bash
python startle.py -w 100 -d 4
```
Start training
> -l stands for level and -f stands for the file which tracks your progress(also --level and --file)
```bash
python startle.py -l 1 -f your_history.txt
```
#### Code:
util/sound.py creates sound waves at given db and duration using Sound Pressure Level formula[^4]
SPL is a measure of the intensity of the sound relative to a reference pressure level. In air, the standard reference pressure is 20 µPa (micropascals), which is considered the threshold of human hearing.
A sine wave is a smooth, periodic oscillation that can be described mathematically by the sine function. The general form of a sine wave is:
y(t)=A⋅sin(2πft+ϕ)
![image](https://github.com/user-attachments/assets/f45b28d4-614e-4716-9e3c-1e2a8b2bbbd8)

The frequency tells us how many complete cycles the sine wave will make in one second.
sample_rate is how many samples per second the waveform will have, set to 44,100 Hz, which is CD quality
Each value in internal_rate_sample corresponds to a specific moment in time during the duration of the sound.
- X-axis (Time in seconds): This represents time, ranging from 0 to 2 seconds.
- Y-axis (Angle in radians): This represents the angle in radians that we pass to the sine function.
- Marking Specific Points: The red dots indicate specific points in time, and the numbers next to them are the calculated angles in radians.
Example:
- At 𝑡 = 0.25 t=0.25 seconds: The angle is approximately 1.57 1.57 radians ( 𝜋 / 2 π/2 radians).
- At 𝑡 = 0.5 t=0.5 seconds: The angle reaches 3.14 3.14 radians (which is 𝜋 π radians).
![image](https://github.com/user-attachments/assets/07a6839a-f4a1-4acd-bbe7-152e49a8c151)


**This process lets you create a sound that theoretically has the desired loudness level (SPL), though actual playback volume will depend on your hardware.**
![SPL](https://www.thermaxxjackets.com/wp-content/uploads/2015/02/Screen-Shot-2015-02-26-at-11.18.51-AM-300x155.png)

startle.py lets you start training and tracks your progress.to trigger startle response makes noise using wav file created by sound.py at random intervals.
Simulates noise at random time intervals to trigger startle response.
Lets user scale how strong was their reaction and does ~~complex~~ basic calculations to get average experience reaction.
Stores this training sessions at given file(--file parameter to set) to track and compare your day to day progress!


>References

[^1]: [hear loss](https://www.nidcd.nih.gov/news/2020/do-you-know-how-loud-too-loud#:~:text=Sound%20is%20measured%20in%20units,dBA%20can%20cause%20hearing%20loss.)

[^2]:  [startle response](https://www.sciencedirect.com/topics/medicine-and-dentistry/startle-response)

[^3]:  [wikipedia](https://en.wikipedia.org/wiki/Startle_response)

[^4]:  [SPL formula](https://blog.thermaxxjackets.com/sound-pressure-math-made-easy)
