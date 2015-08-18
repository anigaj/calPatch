/****************************************************************************
**
** Copyright (C) 2013 Jolla Ltd.
** Contact: Valerio Valerio <valerio.valerio@jolla.com>
**
****************************************************************************/

import QtQuick 2.0
import Sailfish.Silica 1.0
import org.nemomobile.configuration 1.0

Page {
    id: settingsPage

    SilicaFlickable {
        anchors.fill: parent
        contentHeight: column.height

        Column {
            id: column
            width: parent.width

            PageHeader {
                title: "Calendar cover"
            }
           Row {
                width: parent.width
                Label {
                    id: nDaysLabel
                    text: "Show next:"
                     anchors.verticalCenter: nDaysSlider.verticalCenter 
                } 

                Slider {
                    id: nDaysSlider
                    width: 265
                    maximumValue: 31
                    minimumValue: 1
                   stepSize: 1
                   value: calSettings.nDaysForward
                   valueText: value

                   onValueChanged:calSettings.nDaysForward = Math.round(value)
                   onPressAndHold: cancel()
                }
 
                ComboBox {
                   id: dwmComboBox
                   anchors.verticalCenter: nDaysSlider.verticalCenter 
                   //width: parent.width
                   currentIndex:calSettings.daysWeeksMonths 
                   menu: ContextMenu {
                       MenuItem {
                           property int mode: 0
                           text: "Days"
                       }
                       MenuItem {
                           property int mode: 1
                           text: "Weeks" 
                       }
                       MenuItem {
                           property int mode: 2
                           text: "Months"
                       }
                   }
                   onCurrentItemChanged: {
                       if (currentItem) {
                           calSettings.daysWeeksMonths = currentItem.mode
                       }
                   }
               }
            }
                ComboBox {
                   id: leftComboBox 
                   //width: parent.width
                   currentIndex:calSettings.leftAction
                   label: "Left action" 
                   menu: ContextMenu {
                       MenuItem {
                           property int mode: 0
                           text: "Add new event"
                       }
                       MenuItem {
                           property int mode: 1
                           text: "Previous" 
                       }
                       
                   }
                   onCurrentItemChanged: {
                       if (currentItem) {
                           calSettings.leftAction = currentItem.mode
                       }
                   }
               }
                ComboBox {
                   id: rightComboBox 
                   //width: parent.width
                   currentIndex:calSettings.rightAction
                   label: "Right action" 
                   menu: ContextMenu {
                       MenuItem {
                           property int mode: 0
                           text: "Add new event"
                       }
                       MenuItem {
                           property int mode: 1
                           text: "Next" 
                       }
                       
                   }
                   onCurrentItemChanged: {
                       if (currentItem) {
                           calSettings.rightAction = currentItem.mode
                       }
                   }
               }
        }
        VerticalScrollDecorator {}
    }
    ConfigurationGroup {
        id: calSettings
        path: "/apps/jolla-calendar/settings"
        property int nDaysForward: 7
        property int daysWeeksMonths: 0
        property int leftAction: 0
        property int rightAction: 1
    }
}
