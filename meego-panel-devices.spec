Name: meego-panel-devices
Summary: Devices panel
Version: 0.2.7
Release: %mkrel 1
Group: System Environment/Desktop
License: LGPL 2.1
URL: https://www.meego.com
Source0: http://repo.meego.com/MeeGo/releases/1.1/netbook/repos/source/%{name}-%{version}.tar.gz
Requires: mutter-meego
Requires: gthumb
#Requires: gvfs-trash
Requires: GConf2
BuildRequires: libdbus-glib-1-devel
BuildRequires: libcanberra-devel
BuildRequires: libcanberra-gtk-devel
BuildRequires: libpulseaudio-devel >= 0.9.15
BuildRequires: libclutter1.0-devel
BuildRequires: libclutter-gtk0.10-devel
#BuildRequires: devkit-power-gobject-devel
BuildRequires: libGConf2-devel
#BuildRequires: libgdk-x11-2.0-devel
BuildRequires: libnotify-devel
BuildRequires: meego-panel-devel
BuildRequires: mx-devel >= 0.99
BuildRequires: intltool
BuildRequires: gettext
BuildRequires: gnome-common
Obsoletes: moblin-panel-devices < 0.2.7


%description
Meego devices panel


%package test
Summary: Test programs for the devices panel
Group: Development/Tools
Requires: %{name} = %{version}-%{release}

%description test
Programs for testing hardware and software


%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x \
  --disable-static \
  --enable-test-tools

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang meego-panel-devices

%pre
if [ "$1" -gt 1 ]; then
  export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
  gconftool-2 --makefile-uninstall-rule \
    %{_sysconfdir}/gconf/schemas/meego-panel-devices.schemas \
    > /dev/null || : 
fi

%preun
if [ "$1" -eq 0 ]; then
  export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
  gconftool-2 --makefile-uninstall-rule \
    %{_sysconfdir}/gconf/schemas/meego-panel-devices.schemas \
    > /dev/null || : 
fi

%post
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-install-rule \
    %{_sysconfdir}/gconf/schemas/meego-panel-devices.schemas  > /dev/null || : 
/bin/touch --no-create %{_datadir}/icons/hicolor || : 
%{_bindir}/gtk-update-icon-cache \
  --quiet %{_datadir}/icons/hicolor 2> /dev/null|| : 

%postun
/bin/touch --no-create %{_datadir}/icons/hicolor || : 
%{_bindir}/gtk-update-icon-cache \
  --quiet %{_datadir}/icons/hicolor 2> /dev/null|| : 



%files -f meego-panel-devices.lang
%defattr(-,root,root,-)
%doc COPYING
%{_sysconfdir}/gconf/schemas/meego-panel-devices.schemas
%{_sysconfdir}/xdg/autostart/meego-power-icon.desktop
%{_libexecdir}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/theme
%{_datadir}/%{name}/theme/*
%{_datadir}/%{name}/icons/*
%{_datadir}/mutter-meego/panels/%{name}.desktop
%{_datadir}/mutter-meego/panels/meego-power-icon.desktop
%{_datadir}/dbus-1/services/*.service
%{_libexecdir}/meego-power-icon


%files test
%defattr(-,root,root,-)
%{_libdir}/%{name}/*

