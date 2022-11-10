# This is the dummy code from wave documentaion.
# The installing of cypress is not working
# It gives errors like

'''
#
# Fatal error in , line 0
# Failed to deserialize the V8 snapshot blob. This can mean that the snapshot blob file is corrupted or missing.
#
#
#
#FailureMessage Object: 000000083C6FEB30
1: 00007FF6CAE3BCCF node::OnFatalError+69935
2: 00007FF6C5CAE6CA Ordinal0+59082
3: 00007FF6C625CEC8 v8::Isolate::Initialize+744
4: 00007FF6C6D1D48F v8::Isolate::AddMessageListenerWithErrorLevel+1039
5: 00007FF6C9887583 std::__1::vector<v8::CpuProfileDeoptInfo,std::__1::allocator<v8::CpuProfileDeoptInfo> >::max_size+857811
6: 00007FF6C987F89B std::__1::vector<v8::CpuProfileDeoptInfo,std::__1::allocator<v8::CpuProfileDeoptInfo> >::max_size+825835
7: 00007FF6CA28A382 v8_inspector::protocol::Binary::operator=+2434098
8: 00007FF6CA28DC29 v8_inspector::protocol::Binary::operator=+2448601
9: 00007FF6CA289E12 v8_inspector::protocol::Binary::operator=+2432706
10: 00007FF6C9FAB2D0 v8::ExtensionConfiguration::ExtensionConfiguration+2964624
11: 00007FF6C9FAAEEA v8::ExtensionConfiguration::ExtensionConfiguration+2963626
12: 00007FF6C9FA9E57 v8::ExtensionConfiguration::ExtensionConfiguration+2959383
13: 00007FF6C9FAA17D v8::ExtensionConfiguration::ExtensionConfiguration+2960189
14: 00007FF6C97B3167 uv_sleep+2434663
15: 00007FF6CC1EFF02 uv_random+10012786
16: 00007FFFE4B27034 BaseThreadInitThunk+20
17: 00007FFFE4F026A1 RtlUserThreadStart+33

----------

Platform: win32 (10.0.19044)
Cypress Version: 7.2.0

'''

from h2o_wave import cypress


@cypress('Walk through the wizard')
def test_wizard(cy):
    cy.visit('/demo')
    cy.locate('step1').click()
    cy.locate('text').should('contain.text', 'What is your name?')
    cy.locate('nickname').clear().type('Fred')
    cy.locate('step2').click()
    cy.locate('text').should('contain.text',
                             'Hi Fred! How do you feel right now?')
    cy.locate('feeling').clear().type('quirky')
    cy.locate('step3').click()
    cy.locate('text').should('contain.text',
                             'What a coincidence, Fred! I feel quirky too!')
