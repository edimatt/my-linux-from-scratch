%global debug_package %{nil}
%define _build_id_links none
%define system_name htop

Name:           EDO%{system_name}
Version:        3.2.1
Release:        1%{?dist}
Summary:        htop is a cross-platform interactive process viewer.

License:        GPL
URL:            https://github.com/htop-dev/htop
Source0:        %{system_name}-%{version}.tar.gz
Provides:       %{name} = %{version}
BuildRequires:  rpm-build EDOncurses-devel
Requires:       glibc EDOncurses-libs
AutoReqProv:    no

%description
top is a cross-platform interactive process viewer.

htop allows scrolling the list of processes vertically and horizontally
to see their full command lines and related information like memory and
CPU consumption. Also system wide information, like load average or swap
usage, is shown.

The information displayed is configurable through a graphical setup and
can be sorted and filtered interactively.

Tasks related to processes (e.g. killing and renicing) can be done without
entering their PIDs.

Running htop requires ncurses libraries, typically named libncurses(w).

htop is written in C.

For more information and details visit htop.dev.

%prep
%autosetup -n %{system_name}-%{version}
./autogen.sh


%build
%set_build_flags_with_rpath
%configure
%make_build


%install
%make_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%license htop
%doc htop
%_bindir/%{system_name}
%_mandir/man1/%{system_name}.1
%_datadir/applications/*
%_datadir/pixmaps/*
%_datadir/icons/*

%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
