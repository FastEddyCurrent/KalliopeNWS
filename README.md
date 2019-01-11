Synopsis
Give detailed forecast for 1 to 5 days for a given US location no key required.

Installation
kalliope install --git-url https://github.com/FastEddyCurrent/kalliopeNWS.git


Synapse example


---

  - name: "NWSWeather"
    signals:
      - order: "Daily weather please"
    neurons:
      - say:
          message: "NWS Daily Weather"
      - noaa_weather:
          city: "Cleveland"
          state: "Ohio"
          days: 5
          say_template:
              - "{{ content }}"
