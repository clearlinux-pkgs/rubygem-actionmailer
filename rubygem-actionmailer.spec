#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-actionmailer
Version  : 4.2.3
Release  : 3
URL      : https://rubygems.org/downloads/actionmailer-4.2.3.gem
Source0  : https://rubygems.org/downloads/actionmailer-4.2.3.gem
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
%setup -q -D -T -n actionmailer-4.2.3
gem spec %{SOURCE0} -l --ruby > rubygem-actionmailer.gemspec

%build
gem build rubygem-actionmailer.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
actionmailer-4.2.3.gem

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
/usr/lib64/ruby/gems/2.2.0/cache/actionmailer-4.2.3.gem
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/Base/LateAttachmentsProxy/%5b%5d%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/Base/LateAttachmentsProxy/_raise_error-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/Base/LateAttachmentsProxy/cdesc-LateAttachmentsProxy.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/Base/LateAttachmentsProxy/inline-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/Base/NullMail/cdesc-NullMail.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/Base/attachments-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/Base/cdesc-Base.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/Base/controller_path-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/Base/default-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/Base/default_i18n_subject-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/Base/default_options%3d-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/Base/headers-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/Base/mail-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/Base/mailer_name-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/Base/mailer_name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/Base/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/Base/receive-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/Base/register_interceptor-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/Base/register_interceptors-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/Base/register_observer-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/Base/register_observers-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/Base/set_content_type-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/Base/supports_path%3f-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/Collector/all-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/Collector/any-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/Collector/cdesc-Collector.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/Collector/custom-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/Collector/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/Collector/responses-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/DeliveryJob/cdesc-DeliveryJob.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/DeliveryMethods/ClassMethods/add_delivery_method-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/DeliveryMethods/ClassMethods/cdesc-ClassMethods.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/DeliveryMethods/Mail/cdesc-Mail.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/DeliveryMethods/cdesc-DeliveryMethods.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/InlinePreviewInterceptor/cdesc-InlinePreviewInterceptor.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/InlinePreviewInterceptor/data_url-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/InlinePreviewInterceptor/find_part-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/InlinePreviewInterceptor/html_part-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/InlinePreviewInterceptor/html_source-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/InlinePreviewInterceptor/message-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/LogSubscriber/cdesc-LogSubscriber.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/LogSubscriber/deliver-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/LogSubscriber/logger-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/LogSubscriber/process-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/LogSubscriber/receive-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/MailHelper/attachments-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/MailHelper/block_format-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/MailHelper/cdesc-MailHelper.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/MailHelper/format_paragraph-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/MailHelper/mailer-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/MailHelper/message-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/MessageDelivery/cdesc-MessageDelivery.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/MessageDelivery/deliver_later%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/MessageDelivery/deliver_later-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/MessageDelivery/deliver_now%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/MessageDelivery/deliver_now-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/MessageDelivery/enqueue_delivery-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/MessageDelivery/message-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/NonInferrableMailerError/cdesc-NonInferrableMailerError.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/NonInferrableMailerError/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/Preview/all-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/Preview/call-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/Preview/cdesc-Preview.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/Preview/email_exists%3f-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/Preview/emails-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/Preview/exists%3f-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/Preview/find-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/Preview/preview_name-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/Previews/ClassMethods/cdesc-ClassMethods.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/Previews/ClassMethods/register_preview_interceptor-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/Previews/ClassMethods/register_preview_interceptors-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/Previews/cdesc-Previews.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/Railtie/ActiveSupport/cdesc-ActiveSupport.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/Railtie/cdesc-Railtie.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/TestCase/Behavior/ClassMethods/cdesc-ClassMethods.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/TestCase/Behavior/ClassMethods/determine_default_mailer-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/TestCase/Behavior/ClassMethods/mailer_class-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/TestCase/Behavior/ClassMethods/tests-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/TestCase/Behavior/cdesc-Behavior.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/TestCase/Behavior/charset-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/TestCase/Behavior/encode-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/TestCase/Behavior/initialize_test_deliveries-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/TestCase/Behavior/read_fixture-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/TestCase/Behavior/restore_delivery_method-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/TestCase/Behavior/restore_test_deliveries-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/TestCase/Behavior/set_delivery_method-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/TestCase/Behavior/set_expected_mail-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/TestCase/cdesc-TestCase.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/TestHelper/assert_emails-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/TestHelper/assert_no_emails-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/TestHelper/cdesc-TestHelper.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/VERSION/cdesc-VERSION.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/cdesc-ActionMailer.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/gem_version-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ActionMailer/version-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/ApplicationMailer/cdesc-ApplicationMailer.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/Rails/Generators/MailerGenerator/cdesc-MailerGenerator.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/Rails/Generators/MailerGenerator/create_mailer_file-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/Rails/Generators/cdesc-Generators.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/Rails/cdesc-Rails.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/doc/actionmailer-4.2.3/ri/lib/rails/generators/mailer/page-USAGE.ri
/usr/lib64/ruby/gems/2.2.0/gems/actionmailer-4.2.3/CHANGELOG.md
/usr/lib64/ruby/gems/2.2.0/gems/actionmailer-4.2.3/MIT-LICENSE
/usr/lib64/ruby/gems/2.2.0/gems/actionmailer-4.2.3/README.rdoc
/usr/lib64/ruby/gems/2.2.0/gems/actionmailer-4.2.3/lib/action_mailer.rb
/usr/lib64/ruby/gems/2.2.0/gems/actionmailer-4.2.3/lib/action_mailer/base.rb
/usr/lib64/ruby/gems/2.2.0/gems/actionmailer-4.2.3/lib/action_mailer/collector.rb
/usr/lib64/ruby/gems/2.2.0/gems/actionmailer-4.2.3/lib/action_mailer/delivery_job.rb
/usr/lib64/ruby/gems/2.2.0/gems/actionmailer-4.2.3/lib/action_mailer/delivery_methods.rb
/usr/lib64/ruby/gems/2.2.0/gems/actionmailer-4.2.3/lib/action_mailer/gem_version.rb
/usr/lib64/ruby/gems/2.2.0/gems/actionmailer-4.2.3/lib/action_mailer/inline_preview_interceptor.rb
/usr/lib64/ruby/gems/2.2.0/gems/actionmailer-4.2.3/lib/action_mailer/log_subscriber.rb
/usr/lib64/ruby/gems/2.2.0/gems/actionmailer-4.2.3/lib/action_mailer/mail_helper.rb
/usr/lib64/ruby/gems/2.2.0/gems/actionmailer-4.2.3/lib/action_mailer/message_delivery.rb
/usr/lib64/ruby/gems/2.2.0/gems/actionmailer-4.2.3/lib/action_mailer/preview.rb
/usr/lib64/ruby/gems/2.2.0/gems/actionmailer-4.2.3/lib/action_mailer/railtie.rb
/usr/lib64/ruby/gems/2.2.0/gems/actionmailer-4.2.3/lib/action_mailer/test_case.rb
/usr/lib64/ruby/gems/2.2.0/gems/actionmailer-4.2.3/lib/action_mailer/test_helper.rb
/usr/lib64/ruby/gems/2.2.0/gems/actionmailer-4.2.3/lib/action_mailer/version.rb
/usr/lib64/ruby/gems/2.2.0/gems/actionmailer-4.2.3/lib/rails/generators/mailer/USAGE
/usr/lib64/ruby/gems/2.2.0/gems/actionmailer-4.2.3/lib/rails/generators/mailer/mailer_generator.rb
/usr/lib64/ruby/gems/2.2.0/gems/actionmailer-4.2.3/lib/rails/generators/mailer/templates/application_mailer.rb
/usr/lib64/ruby/gems/2.2.0/gems/actionmailer-4.2.3/lib/rails/generators/mailer/templates/mailer.rb
/usr/lib64/ruby/gems/2.2.0/specifications/actionmailer-4.2.3.gemspec
