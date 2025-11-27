import QtQuick
import QtQuick.Controls

ApplicationWindow {
  width: 720
  height: 480
  visible: true
  title: "WizardMerge"
  color: theme.background

  Column {
    anchors.fill: parent
    spacing: 12
    padding: 16

    Rectangle {
      width: parent.width
      height: 64
      color: theme.surface
      radius: 8
      border.color: theme.border
      border.width: 1

      Row {
        anchors.fill: parent
        anchors.margins: 12
        spacing: 12

        Rectangle {
          width: 36
          height: 36
          radius: 18
          color: theme.accent
        }

        Column {
          spacing: 4
          Text {
            text: "WizardMerge"
            font.bold: true
            color: theme.text
            font.pointSize: 18
          }
          Text {
            text: "PyQt6 + QML theming demo"
            color: theme.text
            opacity: 0.7
          }
        }

        Rectangle {
          anchors.verticalCenter: parent.verticalCenter
          width: 1
          height: 40
          color: theme.border
        }

        Text {
          text: `Current theme: ${theme.name}`
          color: theme.text
          anchors.verticalCenter: parent.verticalCenter
        }
      }
    }

    Rectangle {
      width: parent.width
      height: 320
      radius: 8
      color: theme.surface
      border.color: theme.border
      border.width: 1

      Column {
        anchors.fill: parent
        anchors.margins: 16
        spacing: 12

        Text {
          text: "Algorithm preview"
          font.bold: true
          color: theme.text
          font.pointSize: 14
        }

        Rectangle {
          height: 1
          width: parent.width
          color: theme.border
        }

        Text {
          text: "Drop your merge data here. The algorithm preview uses a simple interleaving strategy from wizardmerge.algo.merge.merge_pairs."
          wrapMode: Text.Wrap
          color: theme.text
          opacity: 0.8
        }

        Rectangle {
          width: parent.width
          height: 180
          color: theme.background
          radius: 6
          border.color: theme.border
          border.width: 1
          Text {
            anchors.centerIn: parent
            text: "Future input widgets will live here."
            color: theme.text
            opacity: 0.6
          }
        }
      }
    }
  }
}
