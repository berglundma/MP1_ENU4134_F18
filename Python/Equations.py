# The file with all of the equations

def A(pipe_diameter)
    area = (pi*pipe_diameter^2)/4
    return area;

def G_m(m_dot_f, m_dot_g, pipe_diameter)
    gm=(m_dot_g/A(pipe_diameter))+(m_dot_f/A(pipe_diameter))
    return gm;

# Re_lo = G_m*D/mu_l
# Re_go = G_m*D/mu_g
# f_lo_mc = 0.184Re_lo^-0.2
# rho_m_HEM = 1/((x/rho_g)+((1-x)/rho_f))
# x = m_dot_g/(m_dot_g+m_dot_f)
# g = 9.81

# -dp_dz_HEM = f_lo_mc*G_m^2/(2*D*rho_m_HEM)

# X_tt_squared = (mu_f/mu_g)^0.2*((1-x)/x)^1.8(rho_g/rho_f)
# phi_l_squared = 1+(20/X_tt_squared^(0.5))+(1/X_tt_squared)
# phi_lo_squared_LM = phi_l_squared*(1-x)^(1.8)
# -dp_dz_LM = phi_lo_squared_LM*f_lo_mc*G_m^2/(2*D*rho_l)

# F = x^0.78*(1-x)^0.224
# H = (rho_f/rho_g)^0.91*(mu_g/mu_f)^0.19*(1-(mu_g/mu_f))^0.7
# Fr = G_m^2/(g*D*rho_m_HEM^2)
# We = G_m^2*D/(sigma*rho_m_HEM)
# f_go_fri = (0.86859*ln(Re_go/(1.964*ln(Re_go)-3.8215)))^(-2)
# f_lo_fri = (0.86859*ln(Re_lo/(1.964*ln(Re_lo)-3.8215)))^(-2)
# E = (1-x)^2+x^2*rho_f*f_lo_fri/(rho_g*f_go_fri)
# phi_lo_squared_fri = E+(3.24*F*H/(Fr^0.0454*We^0.035))
# -dp_dz_friedal = f_lo_fri*phi_lo_squared_fri*G_m^2/(2*D*rho_m_HEM)

# n=126

# X_tt_squared_2 = (mu_f/mu_g)^0.2*((1-x)/x)^1.8(rho_g/rho_f)
# phi_l_squared_2 = 1+(C/X_tt_squared^(0.5))+(1/X_tt_squared)
# phi_lo_squared_LM_2 = phi_l_squared*(1-x)^(1.8)
# -dp_dz_LM_2 = phi_lo_squared_LM*f_lo_mc*G_m^2/(2*D*rho_l)

# G_g = (m_dot_g/A)
# G_l = (m_dot_f/A)
# U_sg = rho_f*A/m_dot_f

# Re_l = G_l*D/mu_l
# Re_g = G_g*D/mu_g

# f_lo = C_1*Re_lo^c_2
# f_l = C_1*Re_l^c_2
# f_g = C_1*Re_g^c_2

# f_lo = C_1*Re_lo^c_2
# f_l = C_1*Re_l^c_2
# f_g = C_1*Re_g^c_2

# dp_dz_fric_lo = f_lo*G_m*U_sg/D
# dp_dz_fric_l = f_l*G_m*U_sg/D
# dp_dz_fric_g = f_g*G_m*U_sg/D
