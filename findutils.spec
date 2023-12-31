%global debug_package %{nil}
%define _build_id_links none
%define system_name findutils

Name:           EDO%{system_name}
Version:        4.9.0
Release:        1%{?dist}
Summary:        Directory searching utilities.
License:        GPL
URL:            https://www.gnu.org/software/findutils
Source:         %{system_name}-%{version}.tar.xz
BuildRequires:  rpm-build EDOpcre2-devel libselinux-devel
Requires:       glibc EDOpcre2 libselinux
AutoReqProv:    no

%description
The  GNU  Find Utilities are the basic directory searching utili‐
ties of the GNU operating system. These  programs  are  typically
used  in  conjunction  with other programs to provide modular and
powerful directory search and file locating capabilities to other
commands.

The tools supplied with this package are:

find  ‐  search  for files in a directory hierarchy locate ‐ list
files in databases that match a pattern updatedb ‐ update a  file
name  database xargs ‐ build and execute command lines from stan‐
dard input

The find program searches a directory tree  to  find  a  file  or
group  of  files. It traverses the directory tree and reports all
occurrences of a file matching  the  user’s  specifications.  The
find  program  includes  very powerful searching capability.  The
locate program scans one or more databases of filenames and  dis‐
plays  any  matches. This can be used as a very fast find command
if the file was present during the last file  name  database  up‐
date.   The  updatedb program updates the file name database used
by the locate program. The file name database contains  lists  of
files  that were in particular directory trees when the databases
were last updated. This is usually run nightly by the cron system
daemon.   The  xargs program builds and executes command lines by
gathering together arguments it reads on the standard input. Most
often, these arguments are lists of file names generated by find.


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
%_configure --with-libiconv-prefix=%_prefix --with-libintl-prefix=%_prefix
%make_build


%install
%make_install
# We use mlocate implementation for locate and updatedb.
%__rm %{buildroot}%{_bindir}/{locate,updatedb}
%__rm %{buildroot}%{_mandir}/man1/{locate.1,updatedb.1}
%__rm %{buildroot}%{_mandir}/man5/locatedb.5
%__rm %{buildroot}%{_libdir}/frcode


%clean
rm -rf $RPM_BUILD_ROOT

%files
%_bindir/find
%_bindir/xargs
%_mandir/man1/find.1
%_mandir/man1/xargs.1
%ghost %_infodir/dir
%_infodir/find*
%_datadir/locale/*/LC_MESSAGES/%{system_name}.mo


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
