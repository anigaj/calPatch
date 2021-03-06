Name:          calendar-cover-upcoming
Version:       0.6
Release:       1
Summary:       Calendar cover patch
Group:         System/Patches
Vendor:        Anant Gajjar
Distribution:  SailfisfOS
Packager: Anant Gajjar
License:       GPL
Requires: patchmanager
Requires: sailfish-version >= 3.2.0
BuildArch: noarch

%description
This is a patch for the calendar cover to show the upcoming events. The settings allows configuration of how far ahead to show.

%files
/usr/share/patchmanager/patches/*
/usr/share/jolla-settings/entries/*
/usr/share/jolla-settings/pages/*
/usr/share/jolla-calendar/cover/*
%defattr(-,root,root,-)


%post
%preun
    // Do stuff specific to uninstalls
if [ -f /usr/sbin/patchmanager ]; then
/usr/sbin/patchmanager -u calendar-cover-upcoming || true
fi

%postun
if [ $1 = 0 ]; then
rm -rf /usr/share/patchmanager/patches/calendar-cover-upcoming || true
rm -rf /usr/share/jolla-settings/pages/jolla-calendar || true
rm -rf /usr/share/jolla-settings/entries/jolla-calendar.json || true
else
if [ $1 = 1 ]; then
echo "It's just upgrade"
fi
fi

%changelog
*  Tue Aug 17 2015 Builder <builder@...>
0.6-1
Compatible with Torrunsuo
Change days selection in settings to text field
0.5-1
Compatible with Iijoki
Additional required file is installed rather than part of the patch.
0.4
Remove dependency on calendar
0.3
Added settings
Updated uninstall scripts and dependencies 
0.2
Increased font size
Fixed penultimate event repeat issue
0.1
- First build.
