# based on PLD Linux spec git://git.pld-linux.org/packages/perl-Image-ExifTool.git
%include	/usr/lib/rpm/macros.perl

%define		pdir	Image
%define		pnam	ExifTool

Summary:	Perl module for reading and writing image metadata
Name:		perl-Image-ExifTool
Version:	9.72
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://owl.phy.queensu.ca/~phil/exiftool/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	39363730ca7f58466119c1f6e6562415
URL:		http://www.sno.phy.queensu.ca/~phil/exiftool/
BuildRequires:	perl-devel
BuildRequires:	rpm-perlprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(a)'

%description
ExifTool is a customizable set of Perl libraries plus an application
script for reading and writing meta information in image, audio and
video files.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor \
	destdir=$RPM_BUILD_ROOT
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes html
%attr(755,root,root) %{_bindir}/exiftool
%dir %{perl_vendorlib}/Image/ExifTool
%dir %{perl_vendorlib}/Image/ExifTool/Lang
%{perl_vendorlib}/File/RandomAccess.pm
%{perl_vendorlib}/Image/ExifTool.pm
%{perl_vendorlib}/Image/ExifTool/*.p[lm]
%{perl_vendorlib}/Image/ExifTool/Charset
%lang(de) %{perl_vendorlib}/Image/ExifTool/Lang/de.pm
%lang(pl) %{perl_vendorlib}/Image/ExifTool/Lang/pl.pm
%{_mandir}/man[13]/*

