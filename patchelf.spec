# hardening breaks the set-interpreter-long test on i686, x86_64, ppc64le, s390x
%undefine _hardened_build
%global debug_package %{nil}
%define _build_id_links none
%define system_name patchelf

Name:           EDO%{system_name}
Version:        0.15.0
Release:        2%{?dist}
Summary:        A utility for patching ELF binaries
License:        GPLv3+
URL:            http://nixos.org/patchelf.html
Source0:        https://github.com/NixOS/%{system_name}/archive/%{version}/%{system_name}-%{version}.tar.gz
Patch0:         %{system_name}-%{version}-tests.patch
Provides:       %{name} = %{version}
Requires:       EDOgcc
Requires:       glibc
BuildRequires:  EDOgcc
BuildRequires:  make
BuildRequires:  EDOautoconf
BuildRequires:  EDOautomake
BuildRequires:  EDOcoreutils
AutoReqProv:    no


%description
PatchELF  is  a simple utility for modifying an existing ELF exe‐
cutable or library.  It can change the dynamic loader  ("ELF  in‐
terpreter")  of  an  executable  and  change the RPATH of an exe‐
cutable or library.


%prep
%setup -q -n %{system_name}-%{version}
%patch0 -p1

# package ships elf.h - delete to use glibc-headers one
rm src/elf.h

%build
%set_build_flags_with_rpath
%_configure --docdir=%_docdir/%{name}
%make_build


%check
make check


%install
%make_install

mkdir -p %{buildroot}%{_docdir}/%{name}


%files
%license COPYING
%doc README.md
%{_bindir}/patchelf
%{_mandir}/man1/patchelf.1*


%changelog
* Sun Sep 09 2023 edimatt <edoardo.dimatteo@gmail.com> - 0.15.0-2
- Patch test suite.
- Relocate docs into %{name}.
- Adjust provides and requires.

* Sat Jul 23 2022 Jeremy Sanders <jeremy@jeremysanders.net> - 0.15.0-1
- Update to 0.15.0 (#2107831)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Mar 05 2022 Jeremy Sanders <jeremy@jeremysanders.net> - 0.14.5-1
- Update to 0.14.5 (#2027083)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 10 2021 Jeremy Sanders <jeremy@jeremysanders.net> - 0.13-1
- Update to 0.13 (#1990721)
- Apply patch for self test on ARM

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug 27 2020 Jeremy Sanders <jeremy@jeremysanders.net> - 0.12-1
- Update to 0.12 (#1873104)

* Fri Jul 31 2020 Jeremy Sanders <jeremy@jeremysanders.net> - 0.11-1
- Updated to 0.11 (#1846586)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 03 2019 Dan Horák <dan[at]danny.cz> - 0.10-1
- updated to 0.10 (#1693991)
- enable all arches

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 15 2018 Jeremy Sanders <jeremy@jeremysanders.net> - 0.9-9
- Add gcc-c++ to BuildRequires

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Jeremy Sanders <jeremy@jeremysanders.net> - 0.9-7
- Add gcc and make to BuildRequires

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Aug 14 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.9-1
- Update to patchelf-0.9

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 13 2015 Petr Pisar <ppisar@redhat.com> - 0.8-4
- Adjust to PIC executables (bug #1239761)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Jeremy Sanders <jeremy@jeremysanders.net> - 0.8-1
- Update to patchelf-0.8

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 16 2013 Jeremy Sanders <jeremy@jeremysanders.net> - 0.6-7
- Use macro to exclude all arm builds

* Thu Aug 08 2013 Jeremy Sanders <jeremy@jeremysanders.net> - 0.6-6
- Exclude ARM (bug 627370)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Dec  3 2011 Jeremy Sanders <jeremy@jeremysanders.net> - 0.6-1
- Update to patchelf 0.6
- Preserve ACLs and file based capabilities (fixes #665045)

* Fri Apr  8 2011 Jeremy Sanders <jeremy@jeremysanders.net> - 0.5-9
- Disable building on sparc64 and sparcv9 as self test fails

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 27 2010 Jeremy Sanders <jeremy@jeremysanders.net> - 0.5-7
- Fix typo in man page

* Wed Aug 25 2010 Jeremy Sanders <jeremy@jeremysanders.net> - 0.5-6
- Put new bug number in for ppc/ppc64 issue

* Tue Aug 24 2010 Jeremy Sanders <jeremy@jeremysanders.net> - 0.5-5
- Disable building for ppc/ppc64

* Tue Jun 15 2010 Jeremy Sanders <jeremy@jeremysanders.net> - 0.5-4
- Delete elf.h from source to use native header in glibc-headers

* Mon Jun 14 2010 Jeremy Sanders <jeremy@jeremysanders.net> - 0.5-3
- Corrections from initial review by Martin Gieseking

* Thu Jun 10 2010 Jeremy Sanders <jeremy@jeremysanders.net> - 0.5-2
- Add man page

* Tue Jun  8 2010 Jeremy Sanders <jeremy@jeremysanders.net> - 0.5-1
- Initial package
