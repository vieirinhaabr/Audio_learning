from AudioAnalitcs import AudioAnalitcs


if __name__ == "__main__":
    with AudioAnalitcs:
        print(AudioAnalitcs.getAudio())
        print("OK")
