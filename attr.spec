%global debug_package %{nil}
%define _build_id_links none
%define system_name attr

Name:           EDO%{system_name}
Version:        2.5.2
Release:        2%{?dist}
Summary:        Dynamic library for access control list support.
License:        GPL
Vendor:         %{_vendor}
URL:            https://download-mirror.savannah.gnu.org/releases/attr
Source0:        %{system_name}-%{version}.tar.xz
AutoReqProv:    no
BuildRequires:  glibc-devel 
Requires:       glibc %{name}-libs
Provides:       %{name} = %{version}


%package libs
Summary:        Development tools for the %{system_name} library.
Requires:       glibc
Provides:       %{name}-libs = %{version}
AutoReqProv:    no


%package devel
Summary:        Development tools for the %{system_name} library.
Requires:       %{name}-libs = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description
A set of tools for manipulating extended attributes on filesystem
objects, in particular getfattr(1) and setfattr(1).
An attr(1) command is also provided which is largely compatible
with the SGI IRIX tool of the same name.


%description libs
This package contains the libattr.so dynamic library which contains
the extended attribute system calls and library functions.


%description devel
This  package  contains  header files and documentation needed to
develop programs which make use of extended attributes.  For Lin‐
ux  programs,  the  documented system call API is the recommended
interface, but an SGI IRIX compatibility interface is  also  pro‐
vided.

Currently  only  ext2,  ext3,  ext4  and XFS support extended at‐
tributes.  The SGI IRIX compatibility API built above  the  Linux
system  calls  is  used  by  programs  such as xfsdump(8), xfsre‐
store(8) and xfs_fsr(8).

You should install libattr‐devel if you want to develop  programs
which  make  use of extended attributes.  If you install libattr‐
devel, you’ll also want to install attr.


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
%configure --docdir=%_docdir/%{name}
%make_build


%check
make check


%install
%make_install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%doc ABOUT-NLS
%doc README
%doc CHANGES
%doc COPYING
%doc COPYING.LGPL
%_bindir/%{system_name}
%_bindir/getf%{system_name}
%_bindir/setf%{system_name}
%_mandir/man1/getf%{system_name}.1
%_mandir/man1/setf%{system_name}.1
%_mandir/man1/%{system_name}.1
%_datadir/locale/*/LC_MESSAGES/%{system_name}.mo


%files libs
%_sysconfdir/x%{system_name}.conf
%_libdir/lib%{system_name}.la
%_libdir/lib%{system_name}.so.1*


%files devel
%_includedir/%{system_name}/lib%{system_name}.h
%_includedir/%{system_name}/attributes.h
%_includedir/%{system_name}/error_context.h
%_libdir/pkgconfig/lib%{system_name}.pc
%_libdir/lib%{system_name}.so
%_mandir/man3/%{system_name}_*


%changelog
* Sun Aug 09 2023 edimatt <edoardo.dimatteo@gmail.com> 2.5.1-2
- Disable static library.
- Simplify files section and fix the doc macro.

* Thu Jan 26 2023 Edoardo Di Matteo
- 
