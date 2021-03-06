#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-actionmailer
Version  : 5.0.0.1
Release  : 11
URL      : https://rubygems.org/downloads/actionmailer-5.0.0.1.gem
Source0  : https://rubygems.org/downloads/actionmailer-5.0.0.1.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-rdoc

%description
= Action Mailer -- Easy email delivery and testing
Action Mailer is a framework for designing email service layers. These layers
are used to consolidate code for sending out forgotten passwords, welcome
wishes on signup, invoices for billing, and any other use case that requires
a written notification to either a person or another system.

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n actionmailer-5.0.0.1
gem spec %{SOURCE0} -l --ruby > rubygem-actionmailer.gemspec

%build
export LANG=C
gem build rubygem-actionmailer.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
actionmailer-5.0.0.1.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/actionmailer-5.0.0.1.gem
/usr/lib64/ruby/gems/2.3.0/gems/actionmailer-5.0.0.1/CHANGELOG.md
/usr/lib64/ruby/gems/2.3.0/gems/actionmailer-5.0.0.1/MIT-LICENSE
/usr/lib64/ruby/gems/2.3.0/gems/actionmailer-5.0.0.1/README.rdoc
/usr/lib64/ruby/gems/2.3.0/gems/actionmailer-5.0.0.1/lib/action_mailer.rb
/usr/lib64/ruby/gems/2.3.0/gems/actionmailer-5.0.0.1/lib/action_mailer/base.rb
/usr/lib64/ruby/gems/2.3.0/gems/actionmailer-5.0.0.1/lib/action_mailer/collector.rb
/usr/lib64/ruby/gems/2.3.0/gems/actionmailer-5.0.0.1/lib/action_mailer/delivery_job.rb
/usr/lib64/ruby/gems/2.3.0/gems/actionmailer-5.0.0.1/lib/action_mailer/delivery_methods.rb
/usr/lib64/ruby/gems/2.3.0/gems/actionmailer-5.0.0.1/lib/action_mailer/gem_version.rb
/usr/lib64/ruby/gems/2.3.0/gems/actionmailer-5.0.0.1/lib/action_mailer/inline_preview_interceptor.rb
/usr/lib64/ruby/gems/2.3.0/gems/actionmailer-5.0.0.1/lib/action_mailer/log_subscriber.rb
/usr/lib64/ruby/gems/2.3.0/gems/actionmailer-5.0.0.1/lib/action_mailer/mail_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/actionmailer-5.0.0.1/lib/action_mailer/message_delivery.rb
/usr/lib64/ruby/gems/2.3.0/gems/actionmailer-5.0.0.1/lib/action_mailer/preview.rb
/usr/lib64/ruby/gems/2.3.0/gems/actionmailer-5.0.0.1/lib/action_mailer/railtie.rb
/usr/lib64/ruby/gems/2.3.0/gems/actionmailer-5.0.0.1/lib/action_mailer/rescuable.rb
/usr/lib64/ruby/gems/2.3.0/gems/actionmailer-5.0.0.1/lib/action_mailer/test_case.rb
/usr/lib64/ruby/gems/2.3.0/gems/actionmailer-5.0.0.1/lib/action_mailer/test_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/actionmailer-5.0.0.1/lib/action_mailer/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/actionmailer-5.0.0.1/lib/rails/generators/mailer/USAGE
/usr/lib64/ruby/gems/2.3.0/gems/actionmailer-5.0.0.1/lib/rails/generators/mailer/mailer_generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/actionmailer-5.0.0.1/lib/rails/generators/mailer/templates/application_mailer.rb
/usr/lib64/ruby/gems/2.3.0/gems/actionmailer-5.0.0.1/lib/rails/generators/mailer/templates/mailer.rb
/usr/lib64/ruby/gems/2.3.0/specifications/actionmailer-5.0.0.1.gemspec
