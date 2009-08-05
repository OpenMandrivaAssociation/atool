%define name atool
%define version 0.36.0
%define release %mkrel 2

Summary:        A script for managing file archives of various types
Name:           %{name}
Group:		Archiving/Compression
Version:        %{version}
Release:        %{release}
Source:         http://savannah.nongnu.org/download/atool/%{name}-%{version}.tar.gz
Patch: atool-0.35.0-bash-completion.patch
URL:            http://www.nongnu.org/atool/
License:        GPLv2+
BuildRoot:      %{_tmppath}/%{name}-%{version}-root
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
%patch -p1 -b .bash-completion

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
install -m 644 -D extra/bash-completion-atool_0.1-1 %buildroot%_sysconfdir/bash_completion.d/atool

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README ChangeLog NEWS TODO
%config(noreplace) %_sysconfdir/bash_completion.d/atool
%{_bindir}/*
%{_mandir}/man1/*
