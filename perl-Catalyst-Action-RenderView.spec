%define upstream_name	 Catalyst-Action-RenderView
%define upstream_version 0.16

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Sensible default end action
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Catalyst) >= 5.70
BuildRequires:	perl(Module::Install)
BuildRequires:	perl(Mouse)
BuildRequires:	perl(Data::Visitor)
BuildRequires:	perl(MRO::Compat)
BuildRequires:	perl(HTTP::Request::AsCGI)
BuildRequires:	perl-namespace-clean
BuildArch:	noarch
Requires:	perl(Catalyst) >= 5.70
Requires:	perl(namespace::clean)

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
perl Makefile.PL installdirs=vendor --skipdeps
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/*/*
%{perl_vendorlib}/Catalyst


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.160.0-2mdv2011.0
+ Revision: 680716
- mass rebuild

* Fri Jan 07 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.160.0-1mdv2011.0
+ Revision: 629476
- update to new version 0.16

* Wed Jan 05 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.150.0-1mdv2011.0
+ Revision: 628762
- new version

* Fri Dec 04 2009 Jérôme Quelin <jquelin@mandriva.org> 0.140.0-1mdv2011.0
+ Revision: 473351
- update to 0.14

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.130.0-1mdv2010.1
+ Revision: 461257
- update to 0.13

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.110.0-1mdv2010.0
+ Revision: 406258
- rebuild using %%perl_convert_version

* Mon Jun 29 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.11-1mdv2010.0
+ Revision: 390740
- update to new version 0.11

* Wed May 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.10-1mdv2010.0
+ Revision: 372533
- adding missing prereq
- update to new version 0.10

* Thu Feb 19 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.09-1mdv2009.1
+ Revision: 342949
- update to new version 0.09

* Mon Jul 28 2008 Olivier Thauvin <nanardon@mandriva.org> 0.08-2mdv2009.0
+ Revision: 251708
- buildrequires namespace::clean
- manually add requires to perl-namespace-clean, not find by autoreq/prov

* Tue May 06 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.08-1mdv2009.0
+ Revision: 202326
- update to new version 0.08

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.07-1mdv2008.1
+ Revision: 136666
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Sep 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.07-1mdv2008.0
+ Revision: 78092
- update to new version 0.07

* Sun Sep 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-1mdv2008.0
+ Revision: 78090
- fix build dependencies
- new version

  + Funda Wang <fwang@mandriva.org>
    - BR Module-Install
    - New version


* Tue Jul 04 2006 Scott Karns <scottk@mandriva.org> 0.04-1mdv2007.0
- Version 0.04

* Thu Jun 29 2006 Scott Karns <scottk@mandriva.org> 0.02-1mdv2007.0
- Version 0.02

* Thu Jun 29 2006 Scott Karns <scottk@mandriva.org> 0.01-1mdv2007.0
- First Mandriva release

