%define module	Catalyst-Action-RenderView
%define name	perl-%{module}
%define	modprefix Catalyst

%define version	0.05

%define release	%mkrel 1

Summary:	Sensible default end action
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}/
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{modprefix}/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(Catalyst) >= 5.70
BuildRequires:	perl(Module::Build)
Requires:	perl-Catalyst >= 5.70
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-buildroot

%description
This action implements a sensible default end action, which will
forward to the first available view, unless status is set to 3xx, or
there is a response body. It also allows you to pass dump_info=1 to
the url in order to force a debug screen, while in debug mode.

If you have more than 1 view, you can specify which one to use with
the 'default_view' config setting (See view in Catalyst.)


%prep
%setup -q -n %{module}-%{version}

%build
%__perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/*/*
%{perl_vendorlib}/%{modprefix}

%clean
rm -rf %{buildroot}

