import QtQuick 2.0
import Sailfish.Silica 1.0

Label {
    property bool allDay
    property date startTime
    property date endTime
    property date activeDay


    text: {

       var activeDayStart = new Date(activeDay.getFullYear(), activeDay.getMonth(), activeDay.getDate())
        var tomorrow = new Date(activeDayStart)
        tomorrow.setDate(tomorrow.getDate() + 1)

        var _start = startTime
        var _end = endTime

        if (allDay) {
            //% "All day"
            return qsTrId("All day")
        }

        if (_end.getDate() != _start.getDate()) {
        return (Format.formatDate(_start, Formatter.TimeValue) + "    "
                + Format.formatDate(_end, Formatter.TimeValue))

        }

        return (Format.formatDate(_start, Formatter.TimeValue) + "-"
                + Format.formatDate(_end, Formatter.TimeValue))
    }
}

