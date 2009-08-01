%define upstream_name	 Catalyst-Action-RenderView
%define upstream_version 0.11

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Sensible default end action
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl(Catalyst) >= 5.70
BuildRequires:	perl(Module::Install)
BuildRequires:	perl(Mouse)
BuildRequires:	perl(Data::Visitor)
BuildRequires:	perl(MRO::Compat)
BuildRequires:	perl(HTTP::Request::AsCGI)
BuildRequires:   perl-namespace-clean
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}
Requires:	perl-Catalyst >= 5.70
Requires:   perl-namespace-clean

%description
This action implements a sensible default end action, which will
forward to the first available view, unless status is set to 3xx, or
there is a response body. It also allows you to pass dump_info=1 to
the url in order to force a debug screen, while in debug mode.

If you have more than 1 view, you can specify which one to use with
the 'default_view' config setting (See view in Catalyst.)

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL installdirs=vendor --skipdeps
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/*/*
%{perl_vendorlib}/Catalyst
