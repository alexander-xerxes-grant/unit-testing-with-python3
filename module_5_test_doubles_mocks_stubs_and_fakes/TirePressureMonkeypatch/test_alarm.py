from unittest.mock import Mock, patch

from alarm import (
    Alarm,
)


def test_alarm_with_high_pressure_value():
    with patch("alarm.Sensor") as test_sensor_class:
        test_sensor_instance = Mock()
        test_sensor_instance.sample_pressure.return_value = 22
        test_sensor_class.return_value = test_sensor_instance

        alarm = Alarm()
        alarm.check()

        assert alarm.is_alarm_on
