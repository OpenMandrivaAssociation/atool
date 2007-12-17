%define package atool
%define version 0.33.0
%define release %mkrel 1

Summary:        A script for managing file archives of various types
Name:           %{package}
Group:		Archiving/Compression
Version:        %{version}
Release:        %{release}
Source:         http://savannah.nongnu.org/download/atool/%{package}-%{version}.tar.bz2
URL:            http://www.nongnu.org/atool/
License:        GPL
BuildArch:	noarch
Requires:	perl

%description
atool is a script for managing file archives of various types (tar,
tar+gzip, zip, etc). The main command is probably 'aunpack' which
extracts files from an archive. It overcomes the dreaded "multiple
files in archive root" problem by first extracting to a unique
subdirectory, and then moving back the files if possible. aunpack
also prevents local files from being overwritten by mistake. Other
commands provided are apack (for creating archives), als (for listing
files in archives), and acat (for extracting files to stdout). 

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README ChangeLog NEWS TODO
%{_bindir}/*
%{_mandir}/man1/*
