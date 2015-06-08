Name:          calendar-cover-upcoming
Version:       0.2
Release:       1
Summary:       Calendar cover patch
Group:         System/Patches
Vendor:        Anant Gajjar
Distribution:  SailfisfOS
Packager: Anant Gajjar
License:       GPL

%description
This is a patch for the calendar cover to show the upcoming events for the next seven days.

%files
/usr/share/patchmanager/patches/*

%defattr(-,root,root,-)


%post
%preun
    // Do stuff specific to uninstalls
patchmanager -u calendar-cover-upcoming

%postun
if [ $1 = 0 ]; then
    // Do stuff specific to uninstalls
rm -rf /usr/share/patchmanager/patches/calendar-cover-upcoming
else
if [ $1 = 1 ]; then
    // Do stuff specific to upgrades
echo "It's just upgrade"
fi
fi

%changelog
*  Mon Jun 08 2015 Builder <builder@...> 
0.2
Increased font size
0.1
- First build.
