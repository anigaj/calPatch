Name:          calendar-cover-upcoming
Version:       0.3
Release:       3
Summary:       Calendar cover patch
Group:         System/Patches
Vendor:        Anant Gajjar
Distribution:  SailfisfOS
Packager: Anant Gajjar
License:       GPL
Requires: patchmanager
Requires: jolla-calendar <= 0.6.3

%description
This is a patch for the calendar cover to show the upcoming events. The settings allows configuration of how far ahead to show.

%files
/usr/share/patchmanager/patches/*
/usr/share/jolla-settings/entries/*
/usr/share/jolla-settings/pages/*

%defattr(-,root,root,-)


%post
%preun
    // Do stuff specific to uninstalls
if [ -f /usr/sbin/patchmanager ]; then
/usr/sbin/patchmanager -u calendar-cover-upcoming || true
rm -f /usr/share/jolla-calendar/cover/CoverTimeLabel.qml || true
fi

%postun
if [ $1 = 0 ]; then
    // Do stuff specific to uninstalls
rm -rf /usr/share/patchmanager/patches/calendar-cover-upcoming || true
rm -rf /usr/share/jolla-settings/pages/jolla-calendar || true
rm -rf /usr/share/jolla-settings/entries/jolla-calendar.json || true
else
if [ $1 = 1 ]; then
    // Do stuff specific to upgrades
echo "It's just upgrade"
fi
fi

%changelog
*  Tue Aug 17 2015 Builder <builder@...>
0.3
Added settings
Updated uninstall scripts and dependencies 
0.2
Increased font size
Fixed penultimate event repeat issue
0.1
- First build.
